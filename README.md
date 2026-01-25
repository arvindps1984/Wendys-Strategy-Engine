# Wendys-Strategy-Engine
A multi-agent strategic orchestrator built with LangGraph to design evidence-backed, brand-aligned offers for Wendy's

🍔 Wendy's Strategy Engine: Multi-Agent Offer Design Board
FreshAi is an advanced strategic orchestration system built on LangGraph. It replaces traditional, manual marketing brainstorms with a data-driven "Strategy Board" that synthesizes competitive whitespaces, customer behavioral signals, and emerging market trends into actionable, brand-aligned offer concepts.

🎯 Hackathon Rubric Alignment
Signal Quality & Depth (S): Our system utilizes a Recency-Biased Threat Score model that weights competitor actions by their freshness (exponential decay) and market saturation. Every insight is tagged with a unique Traceability ID for data auditing.

Offer Creativity (O): Beyond standard discounts, our Master Orchestrator is programmed to identify "Strategic Pivots"—identifying high-velocity trends with low competitor coverage to suggest bold, first-to-market moves.

Agent Collaboration (A): This project features a stateful Fan-In/Fan-Out architecture. Parallel specialized analysts (Competitor, Customer, Trends) feed into a centralized Orchestrator, followed by a Brand Validator loop to ensure Wendy’s signature challenger voice.

🏗️ Technical Architecture
The system is built using a directed acyclic graph (DAG) structure:

Phase 1: Specialized Intelligence (Parallel)

CompetitorAnalyst: Calculates threat scores based on gaps in Wendy’s current promo stack.

CustomerAnalyst: Extracts behavioral segments and redemption elasticities.

TrendAnalyst: Scans social velocity for emerging mechanics like "Gamification" and "Subscriptions".

Phase 2: Strategy Synthesis

OfferDesigner: Fuses signals to create evidence-backed concepts.

BrandValidator: Refines the output for Wendy's "Fresh, never frozen" personality.

Phase 3: Executive Visualization

ScorecardVisualizer: Generates a Feasibility vs. Impact matrix for immediate decision-making.

🛠️ Installation & Setup
Prerequisites
Python 3.9+

TigerAnalytics AI Gateway Access (OpenAI-compatible)

Setup:

1. Clone the Repository:
    git clone https://github.com/your-username/Wendys-Strategy-Engine.git
    cd wendys-Wendys-Strategy-Engine

2. Install Dependencies:
   pip install -r requirements.txt

3. Configure Secrets: Create a .streamlit/secrets.toml file (locally) or set up Streamlit Cloud Secrets:
   TIGER_API_KEY = "your_api_key_here"

4. Run the App:
   streamlit run app.py

📊 Sample Output
Defensive Concept: "Wendy's Streak Week" — Combines app-savviness with gamification to counter competitor loyalty threats.
Strategic Pivot: "The Fresh Fry Subscription" — Leverages the subscription trend (+113% growth) where competition is currently low.

👥 The Team
Team Name: Team 13 - AI Alchemists
Hackathon: TigerAnalytics Hackathon 2026
