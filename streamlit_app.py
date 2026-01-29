# streamlit_app.py

import streamlit as st
import pandas as pd
from engine import app  

st.set_page_config(
    page_title="Wendy’s Signal-to-Offer Engine",
    layout="wide"
)

st.title("🍔 Wendy’s Signal-to-Offer Engine")
st.caption("Turning market signals into launch-ready offers — with evidence.")

st.markdown("""
This system converts fragmented market noise into **prioritized, evidence-backed offers**  
by orchestrating multiple AI agents across competition, customers, and trends.
""")

st.divider()

# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------
st.subheader("1️⃣ Configure Current Wendy’s Context")

wendys_active = st.multiselect(
    "Select currently active Wendy’s offers:",
    options=[
        "Biggie Bag",
        "4 for $4",
        "Breakfast Combo",
        "Frosty Promo",
        "Rewards Multiplier"
    ],
    default=["Biggie Bag", "4 for $4"]
)

run_button = st.button("🚀 Generate Offers", type="primary")

# ---------------------------------------------------------
# EXECUTION
# ---------------------------------------------------------
if run_button:
    with st.spinner("Running multi-agent analysis..."):
        result = app.invoke({
            "wendys_active": wendys_active
        })

    st.success("Analysis complete")

    st.divider()
    st.header("🔍 Agent Intelligence")

    with st.expander("🧠 Competitor Intelligence"):
        st.text(result["competitor_intel"]["summary"])

    with st.expander("👤 Customer Insights"):
        st.text(result["customer_insights"])

    with st.expander("📈 Market Trends & Timing"):
        st.markdown(result["market_trends_summary"])
        st.json(result["market_context_windows"])

    st.divider()
    st.header("🎨 Designed Wendy’s Offers")

    st.markdown(result["final_report_text"])

    for offer in result["structured_concepts"]:
        with st.container(border=True):
            st.subheader(offer["name"])
            st.write(offer["witty_rationale"])

            cols = st.columns(4)
            cols[0].metric("Type", offer["type"])
            cols[1].metric("Feasibility", offer["feasibility"])
            cols[2].metric("Impact", offer["impact"])
            cols[3].metric(
                "Confidence",
                round((offer["impact"] + offer["feasibility"]) / 20, 2)
            )

            st.caption(
                f"Evidence Signals: {', '.join(offer['evidence_signals'])}"
            )

    st.divider()
    st.header("📊 Executive Prioritization View")

    st.markdown(
        "**Higher impact + feasibility should be prioritized for immediate launch.**"
    )

    st.dataframe(
        result["prioritization_table"],
        use_container_width=True
    )
