# -*- coding: utf-8 -*-
import json

def offer_designer_node(state, client, MODEL_NAME, TREND_MECHANIC_MAP):
    """Fuses intelligence signals into differentiated strategic offers."""
    prompt = f"""
    Design 1 Defensive response and 1 First-to-Market pivot.
    COMPETITOR GAPS: {state['competitor_intel']['summary']}
    CUSTOMER INSIGHTS: {state['customer_insights']}
    TRENDS: {state['market_trends_summary']}
    CONSTRAINTS: {json.dumps(TREND_MECHANIC_MAP)}
    """
    res = client.chat.completions.create(model=MODEL_NAME, messages=[{"role": "user", "content": prompt}])
    return {"raw_concepts": res.choices[0].message.content}
