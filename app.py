import streamlit as st
from engine import get_strategy_app, MasterState
from openai import OpenAI

# 1. SIDEBAR CONFIGURATION
st.sidebar.header("🔐 API Configuration")
try:
    openai_api_key = st.secrets["TIGER_API_KEY"]
    client = OpenAI(api_key=openai_api_key, base_url="https://api.ai-gateway.tigeranalytics.com")
except Exception:
    st.error("🔑 API Key not found. Please configure TIGER_API_KEY in your Streamlit Secrets.")
    st.stop()

# 2. INITIALIZE ENGINE
agent_app = get_strategy_app(client) # Use the function from engine.py

# 3. UI PARAMETERS
st.sidebar.header("🎯 Strategy Parameters")
wendys_current = st.sidebar.multiselect(
    "Wendy's Currently Active Promos",
    ["Biggie Bag", "4 for $4", "Breakfast 2 for $3", "BOGO Dave's Single"],
    default=["Biggie Bag", "4 for $4"]
)

# 4. TRIGGER BUTTON
if st.sidebar.button("🚀 Generate Fresh Strategy"):
    with st.spinner("Executing multi-agent analysis..."):
        # The engine logic stays in engine.py, the results come back here
        result = agent_app.invoke({"wendys_active": wendys_current})
        
        # ... Rest of your st.markdown and st.write logic for Phase 1, 2, and 3 ...
        st.success("Analysis Complete!")
