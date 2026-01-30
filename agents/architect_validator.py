# -*- coding: utf-8 -*-
import json

def brand_validator_node(state, client, MODEL_NAME):
    """Acts as the quality gate for brand voice and data integrity."""
    prompt = f"Refine these concepts into Wendy's witty brand voice: {state['raw_concepts']}"
    res = client.chat.completions.create(
        model=MODEL_NAME,
        response_format={"type": "json_object"},
        messages=[{"role": "user", "content": prompt}]
    )
    data = json.loads(res.choices[0].message.content)
    return {"structured_concepts": data["offers"], "final_report_text": data["report_intro"]}
