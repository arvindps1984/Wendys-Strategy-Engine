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


### Project Architecture

```mermaid

graph TD
    %% Global Styling
    accTitle: Wendy's Signal-to-Offer Engine Architecture
    accDescr: Multi-agent orchestration flow from signal to scorecard

    %% Entry Point
    Start([User Input: Active Promos]) --> UI[Streamlit Frontend]
    UI --> StateInit{Initialize MasterState}

    %% Phase 1: Signal Intelligence (Parallel Fan-Out)
    subgraph Phase_1 [Phase 1: Signal Intelligence]
        direction LR
        StateInit --> Comp[Competitor Analyst Agent]
        StateInit --> Cust[Customer Insights Agent]
        StateInit --> MktGen[Market Context Generator]
        
        MktGen --> MktCtx[Market Context Analyst]
        MktCtx --> Trend[Market Trends Narrator]
    end

    %% Sync point
    Comp --> Sync{Sync Intelligence}
    Cust --> Sync
    Trend --> Sync

    %% Phase 2: Design & Brand (Sequential Fan-In)
    subgraph Phase_2 [Phase 2: Design & Brand Alignment]
        Sync --> Designer[Offer Designer Agent]
        Designer -- "Raw Offer Concepts" --> Validator[Brand Validator Agent]
        Validator -- "Witty Rationale & JSON" --> Finalize[Finalize State]
    end

    %% Phase 3: Executive Review
    subgraph Phase_3 [Phase 3: Executive Scorecard]
        Finalize --> Viz[Visualization Node]
        Viz -- "Prioritization Table" --> Dashboard[Streamlit Dashboard]
    end

    %% End Result
    Dashboard --> End([Final Strategy & Balloons])

    %% High-Contrast Class Definitions
    classDef default fill:#FFFFFF,stroke:#333333,stroke-width:2px,color:#000000;
    classDef startNode fill:#FFDDE1,stroke:#EE2737,stroke-width:3px,color:#000000,font-weight:bold;
    classDef agentNode fill:#F0F4C3,stroke:#827717,stroke-width:2px,color:#000000;
    classDef syncNode fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#000000;

    %% Applying Classes
    class Start,End startNode;
    class Comp,Cust,MktGen,MktCtx,Trend,Designer,Validator,Viz agentNode;
    class Sync,StateInit syncNode;

    %% Subgraph (Phase) Branding with High Contrast
    style Phase_1 fill:#FFF9C4,stroke:#FBC02D,stroke-width:4px,color:#000000,font-weight:bold;
    style Phase_2 fill:#E3F2FD,stroke:#1976D2,stroke-width:4px,color:#000000,font-weight:bold;
    style Phase_3 fill:#E8F5E9,stroke:#388E3C,stroke-width:4px,color:#000000,font-weight:bold;
\```

