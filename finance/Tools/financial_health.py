def financial_health(income, expenses):
    ratio = expenses / income if income > 0 else 1

    if ratio > 0.9:
        return "Critical"
    elif ratio > 0.7:
        return "Warning"
    return "Healthy"