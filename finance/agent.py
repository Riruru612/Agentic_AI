import os
from dotenv import load_dotenv

from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq

# Import your main tool
from finance.Tools.finance_tool import finance_analysis


# 🔐 Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")


# 🧰 Tools list (only one main tool like your team)
tools = [finance_analysis]


# 🧠 LLM setup (Groq)
llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=GROQ_API_KEY
)


# 🤖 Agent setup (same as business agent)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# 🚀 Run loop
if __name__ == "__main__":

    print("Finance Agent Ready (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        try:
            response = agent.run(query)
            print("\nFinance Report:\n", response)

        except Exception as e:
            print("Error:", str(e))