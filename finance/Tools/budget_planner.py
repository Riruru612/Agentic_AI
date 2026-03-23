def suggest_budget(income):
    return {
        "needs": round(income * 0.5, 2),
        "wants": round(income * 0.3, 2),
        "savings": round(income * 0.2, 2)
    }