import streamlit as st
import pandas as pd
from engine import get_strategy_app  # Ensure engine.py is in the same folder
from openai import OpenAI

# --- 1. UI & PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Wendy's FreshAi Strategy Board", 
    layout="wide", 
    page_icon="🍔",
    initial_sidebar_state="collapsed"
)

# Custom CSS to completely hide the sidebar and the toggle arrow for a clean UI
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# --- 2. SILENT API CONFIGURATION ---
# No sidebar elements. Logic runs silently; stops only if keys are missing.
try:
    openai_api_key = st.secrets["TIGER_API_KEY"]
    client = OpenAI(
        api_key=openai_api_key, 
        base_url="https://api.ai-gateway.tigeranalytics.com"
    )
    # Initialize the LangGraph engine
    agent_app = get_strategy_app(client)
except Exception:
    st.error("🔑 API Key not found. Please ensure TIGER_API_KEY is set in your Streamlit Secrets.")
    st.stop()

# --- 3. HEADER SECTION (Reflecting Screenshot 1) ---
st.title("🍔 Wendy's Signal-to-Offer Engine")
st.markdown("##### Turning market signals into launch-ready offers — with evidence.")
st.write("This system converts fragmented market noise into prioritized, evidence-backed offers by orchestrating multiple AI agents across competition, customers, and trends.")

st.divider()

# --- 4. CONTEXT CONFIGURATION (Reflecting Screenshot 2) ---
st.markdown("### 1️⃣ Configure Current Wendy’s Context")
st.write("Select currently active Wendy's offers:")

wendys_current = st.multiselect(
    "Select currently active Wendy's offers:",
    options=["Biggie Bag", "4 for $4", "Breakfast 2 for $3", "BOGO Dave's Single"],
    default=["Biggie Bag", "4 for $4"],
    label_visibility="collapsed"
)

# Main page button for generation
if st.button("🚀 Generate Offers"):
    with st.spinner("Executing multi-agent analysis..."):
        # Invoke the compiled LangGraph engine from engine.py
        result = agent_app.invoke({"wendys_active": wendys_current})

        # --- PHASE 1: SIGNAL INTELLIGENCE ---
        st.markdown("## 🔎 Phase 1: Signal Intelligence")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("**Competitor Intelligence**")
            st.write(result.get("competitor_intel", {}).get("summary", "N/A"))
        with col2:
            st.success("**Customer Insights**")
            st.write(result.get("customer_insights", "N/A"))
        with col3:
            st.warning("**Market Trends**")
            st.write(result.get("market_trends_summary", "N/A"))

        st.divider()

        # --- PHASE 2: DESIGN & BRAND ALIGNMENT ---
        st.markdown("## ✨ Phase 2: Design & Brand Alignment")
        st.write(f"*{result.get('final_report_text', 'Generating report...')}*")
        
        offers = result.get("structured_concepts", [])
        for offer in offers:
            with st.expander(f"Offer: {offer['name']} ({offer['type']})", expanded=True):
                # Displays rationale with safety check for key names
                st.write(offer.get("rationale", offer.get("witty_rationale", "No rationale provided.")))

        st.divider()

        # --- PHASE 3: EXECUTIVE SCORECARD ---
        st.markdown("## 📊 Phase 3: Executive Prioritization Scorecard")
        
        df_scorecard = result.get("prioritization_table")
        if df_scorecard is not None:
            # Heat-map styling for Feasibility and Impact
            st.dataframe(
                df_scorecard.style.background_gradient(cmap='YlOrRd', subset=['Feasibility', 'Impact']),
                use_container_width=True
            )
        
        st.balloons()
