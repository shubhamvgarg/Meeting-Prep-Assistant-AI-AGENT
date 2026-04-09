from langchain_groq import ChatGroq
from tools.tavily_search import search

llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

def company_agent(state):
    company = state["company"]

    results = search(f"{company} company overview recent news")

    prompt = f"""
    Analyze the following data about {company}:
    {results}

    Provide:
    - Company overview
    - Key products/services
    - Recent developments
    """

    response = llm.invoke(prompt)

    return {"company_info": response.content}