🍔 Wendy’s Signal-to-Offer Engine
Wendy’s Signal-to-Offer Engine is an AI-native strategic orchestrator that converts fragmented market noise into prioritized, evidence-backed marketing offers. Built using LangGraph and Streamlit, it simulates a digital "Boardroom" of specialized AI agents that analyze competitor threats, customer behavioral patterns, and high-velocity market trends in real-time.

🎯 The Problem
In the fast-paced QSR (Quick Service Restaurant) industry, marketing teams often struggle with "analysis paralysis." Decisions are often made based on stale data or gut feeling rather than a synthesized view of the entire market landscape.

🚀 The Solution
Our engine uses a Parallel Fan-Out architecture to ensure that every creative offer is grounded in multi-dimensional evidence. By the time a strategy reaches the executive scorecard, it has been:

Analyzed for competitive threat levels.

Validated against customer redemption patterns.

Timed to match emerging market context (e.g., Payday, Weather, or Social Trends).

Refined into Wendy’s signature "witty" brand voice.

🏗 Project Architecture
The system is orchestrated as a stateful graph where intelligence is gathered in parallel before being synthesized by a creative lead.

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
```
