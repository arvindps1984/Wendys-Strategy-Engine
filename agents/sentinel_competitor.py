# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random

def competitor_analyst_node(state, fake, TODAY):
    """Calculates advanced Threat Scores: Saturation + Velocity + Recency Bias."""
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
        score = round(min(10.0, group['weight'].sum() / 5), 1)
        trace_id = group.sort_values('weight', ascending=False)['id'].iloc[0]
        threats.append(f"{mech} driven by {top_brand} (Threat: {score}/10) [Ref ID: {trace_id}]")
    return {"competitor_intel": {"summary": "\n".join(threats), "raw": gaps.to_dict()}}
