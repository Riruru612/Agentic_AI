from langchain.tools import tool
import re

from finance.Tools.profit_calculator import calculate_profit
from finance.Tools.budget_planner import suggest_budget
from finance.Tools.financial_health import financial_health


@tool
def finance_analysis(query: str):
    """
    Perform financial analysis based on user query
    """

    # 🔍 Extract numbers from query
    numbers = list(map(int, re.findall(r'\d+', query)))

    if len(numbers) >= 2:
        revenue = numbers[0]
        expenses = numbers[1]
    else:
        # fallback values
        revenue = 50000
        expenses = 30000

    # 🧠 Call tools
    profit_data = calculate_profit(revenue, expenses)
    budget = suggest_budget(revenue)
    health = financial_health(revenue, expenses)

    return {
        "summary": f"Profit: {profit_data['profit']}",
        "details": {
            "revenue": revenue,
            "expenses": expenses,
            "profit_analysis": profit_data,
            "budget": budget,
            "financial_health": health
        }
    }