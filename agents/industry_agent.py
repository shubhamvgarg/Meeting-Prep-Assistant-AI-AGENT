from langchain_groq import ChatGroq
from tools.tavily_search import search

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def industry_agent(state):
    company = state["company"]

    results = search(f"{company} industry trends challenges opportunities")

    prompt = f"""
    Based on this data:
    {results}

    Provide:
    - Industry trends
    - Risks
    - Opportunities
    """

    response = llm.invoke(prompt)

    return {"industry_insights": response.content}