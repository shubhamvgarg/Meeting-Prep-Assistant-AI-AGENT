from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def brief_agent(state):
    prompt = f"""
    Create a clean, executive-ready meeting brief.

    Strategy:
    {state['strategy']}

    Format:
    - Summary
    - Key Insights
    - Talking Points
    - Questions
    """

    response = llm.invoke(prompt)

    return {"brief": response.content}