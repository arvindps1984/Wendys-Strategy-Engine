import pandas as pd
import numpy as np
import random
import json
from typing import TypedDict, List
from faker import Faker
from openai import OpenAI
from datetime import date
from langgraph.graph import StateGraph, START, END

# --- CONFIGURATION & SETUP ---
# Note: In a production environment, ensure API keys are managed via environment variables
# For this script, we assume the OpenAI client is initialized outside or via a mock for the engine.
# In your app.py, you would initialize this client using st.secrets.

fake = Faker()
TODAY = date(2026, 1, 24)
MODEL_NAME = "gemini-2.5-flash"

# --- MASTER STATE DEFINITION ---
class MasterState(TypedDict):
    wendys_active: List[str]
    competitor_intel: dict
    customer_insights: str
    raw_market_signals: pd.DataFrame
    market_trends: List[dict]
    market_context_windows: List[dict]
    market_trends_summary: str
    raw_concepts: str
    structured_concepts: List[dict]
    final_report_text: str
    prioritization_table: pd.DataFrame

# Mapping for trend-to-mechanic alignment
TREND_MECHANIC_MAP = {
    "Gamified Rewards": "challenge, streak, or unlock mechanic",
    "Late-Night Value": "time-boxed or after-hours unlock",
    "Surprise & Delight": "randomized reward trigger",
    "Subscription Meal Bundles": "recurring opt-in benefit",
    "App-Exclusive Perks": "mobile-only gated access"
}

# --- AGENT NODES (CORE LOGIC) ---

def competitor_analyst_node(state: MasterState):
    """Calculates advanced Threat Scores with Recency Bias."""
    records = []
    for _ in range(500):
        records.append({
            "id": fake.uuid4()[:8],
            "brand": random.choice(["McDonald's", "Burger King", "Taco Bell"]),
            "mechanic": random.choice(["BOGO", "Gamified App Challenge", "Loyalty Multiplier"]),
            "obs_date": pd.to_datetime(fake.date_between(start_date='-60d', end_date=TODAY))
        })
    df = pd.DataFrame(records)
    df['weight'] = np.exp(-0.05 * (pd.Timestamp(TODAY) - df['obs_date']).dt.days)

    gaps = df[~df['mechanic'].isin(state["wendys_active"])].copy()
    threats = []
    for mech, group in gaps.groupby('mechanic'):
        top_brand = group.groupby('brand')['weight'].sum().idxmax()
        score = round(min(10, (group['weight'].sum() / 5)), 1)
        trace_id = group.sort_values('weight', ascending=False)['id'].iloc[0]
        threats.append(f"{mech} driven by {top_brand} (Threat: {score}/10) [Ref ID: {trace_id}]")

    return {"competitor_intel": {"summary": "\n".join(threats), "raw": gaps.to_dict()}}

def customer_analyst_node(state: MasterState):
    """Analyzes behavioral signals for segments."""
    insights = [
        "Value-Oriented Mobile Users redeem app offers 1.002x more often.",
        "Efficient Drive-Thru Diners redeem 1.004x more often via Drive-Thru."
    ]
    return {"customer_insights": "\n".join(insights)}

def market_context_generator(state: MasterState):
    """Generates synthetic market signals."""
    records = []
    trend_types = ["Gamified Rewards", "Subscription Meal Bundles", "Surprise & Delight", "Late-Night Value", "App-Exclusive Perks"]
    seasons, dayparts = ["Winter", "Spring", "Summer", "Fall"], ["Breakfast", "Lunch", "Dinner", "Late Night"]
    situations, sources = ["Cold Weather", "Payday", "Commute", "Weekend"], ["Reddit", "TikTok", "Press", "Food Blogs"]

    for _ in range(900):
        records.append({
            "trend_type": random.choice(trend_types),
            "season": random.choice(seasons),
            "daypart": random.choice(dayparts),
            "situation": random.choice(situations),
            "source": random.choice(sources),
            "observed_date": fake.date_between(start_date='-120d', end_date=TODAY)
        })
    return {"raw_market_signals": pd.DataFrame(records)}

def market_context_analyst(state: MasterState):
    """Scores market context based on strength and recency."""
    df = state["raw_market_signals"].copy()
    df["observed_date"] = pd.to_datetime(df["observed_date"])
    df["weight"] = np.exp(-0.05 * (pd.Timestamp(TODAY) - df["observed_date"]).dt.days)

    windows = []
    for keys, group in df.groupby(["trend_type", "season", "daypart", "situation"]):
        strength = group["weight"].sum()
        windows.append({
            "signal_id": f"CTX-{group.index[0]}",
            "trend": keys[0], "season": keys[1], "daypart": keys[2], "situation": keys[3],
            "timing_strength": round(strength, 2)
        })

    if not windows: return {"market_context_windows": []}
    max_strength = max(w["timing_strength"] for w in windows)
    for w in windows:
        w["relevance_score"] = round((w["timing_strength"] / max_strength) * 10, 1)
        w["action"] = "Act Now" if w["relevance_score"] >= 7 else "Monitor"

    return {"market_context_windows": sorted(windows, key=lambda x: x["relevance_score"], reverse=True)[:5]}

def market_trends_narrator(state: MasterState, client: OpenAI):
    """Converts signals to a narrative summary."""
    context = json.dumps(state["market_context_windows"], indent=2)
    prompt = f"Summarize top emerging trends based on these signals:\n{context}"
    res = client.chat.completions.create(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return {"market_trends_summary": res.choices[0].message.content}

def offer_designer_node(state: MasterState, client: OpenAI):
    """Fuses intelligence into creative offer concepts."""
    prompt = f"""
    Design 2 Wendy's offers (1 Defensive, 1 First-to-Market).
    COMPETITOR GAPS: {state['competitor_intel']['summary']}
    CUSTOMER INSIGHTS: {state['customer_insights']}
    TRENDS: {state['market_trends_summary']}
    TOP SIGNALS: {json.dumps(state["market_context_windows"], indent=2)}
    """
    res = client.chat.completions.create(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return {"raw_concepts": res.choices[0].message.content}

def brand_validator_node(state: MasterState, client: OpenAI):
    """Refines concepts into brand voice and strictly enforces the JSON structure."""
    prompt = f"""
    Refine these concepts into Wendy's witty, fresh brand voice: {state['raw_concepts']}

    YOU MUST RETURN A JSON OBJECT WITH EXACTLY THESE TWO TOP-LEVEL KEYS:
    1. 'report_intro': A 2-sentence witty overall summary.
    2. 'offers': A list of objects, each containing: 
       'name', 'rationale', 'type', 'feasibility' (1-10), 'impact' (1-10).
    """
    
    try:
        res = client.chat.completions.create(
            model=MODEL_NAME,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}]
        )
        # Parse the JSON response
        data = json.loads(res.choices[0].message.content)
        
        # Safety check: Ensure 'data' is a dictionary and contains 'offers'
        if not isinstance(data, dict):
            raise ValueError("LLM did not return a dictionary")
            
        return {
            "structured_concepts": data.get("offers", []), 
            "final_report_text": data.get("report_intro", "Strategy generated successfully.")
        }
        
    except Exception as e:
        # Fallback logic to prevent the app from crashing
        st.error(f"⚠️ Brand Validation Error: {e}")
        return {
            "structured_concepts": [], 
            "final_report_text": "Error refining strategy voice. Please try again."
        }
def visualization_node(state: MasterState):
    """Dynamically builds a prioritization table with safety checks for missing keys."""
    concepts = state.get("structured_concepts", [])
    
    table_data = []
    for item in concepts:
        # Use .get() to avoid KeyError if the LLM misses a field
        name = item.get("name", "Unnamed Concept")
        feasibility = item.get("feasibility", 5.0) # Default to 5.0 if missing
        impact = item.get("impact", 5.0)
        ctype = item.get("type", "N/A")
        
        table_data.append({
            "Concept": name,
            "Feasibility": feasibility,
            "Impact": impact,
            "Confidence": round((impact + feasibility) / 20, 2),
            "Type": ctype
        })

    # Return the DataFrame for the scorecard
    return {"prioritization_table": pd.DataFrame(table_data)}

# --- GRAPH ASSEMBLY FUNCTION ---

def get_strategy_app(client: OpenAI):
    """Compiles and returns the LangGraph application."""
    builder = StateGraph(MasterState)
    
    # Add nodes
    builder.add_node("comp", competitor_analyst_node)
    builder.add_node("cust", customer_analyst_node)
    builder.add_node("mkt_gen", market_context_generator)
    builder.add_node("mkt_ctx", market_context_analyst)
    builder.add_node("trend", lambda state: market_trends_narrator(state, client))
    builder.add_node("design", lambda state: offer_designer_node(state, client))
    builder.add_node("validate", lambda state: brand_validator_node(state, client))
    builder.add_node("viz", visualization_node)

    # Define edges
    builder.add_edge(START, "comp")
    builder.add_edge(START, "cust")
    builder.add_edge(START, "mkt_gen")
    builder.add_edge("mkt_gen", "mkt_ctx")
    builder.add_edge("mkt_ctx", "trend")
    builder.add_edge("trend", "design")
    builder.add_edge("design", "validate")
    builder.add_edge("validate", "viz")
    builder.add_edge("viz", END)

    return builder.compile()
