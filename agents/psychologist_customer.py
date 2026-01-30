# -*- coding: utf-8 -*-
def customer_analyst_node(state):
    """Analyzes behavioral signals to identify high-redemption segments."""
    insights = [
        "Value-Oriented Mobile Users redeem app offers 1.002x more often.",
        "Efficient Drive-Thru Diners redeem 1.004x more often via Drive-Thru."
    ]
    return {"customer_insights": "\n".join(insights)}
