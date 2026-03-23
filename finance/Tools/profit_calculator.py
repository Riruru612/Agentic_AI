def calculate_profit(revenue, expenses):
    profit = revenue - expenses

    return {
        "profit": profit,
        "margin": (profit / revenue) * 100 if revenue > 0 else 0,
        "status": "profit" if profit > 0 else "loss"
    }