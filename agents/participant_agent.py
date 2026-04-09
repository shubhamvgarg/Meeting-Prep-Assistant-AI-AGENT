from langchain_groq import ChatGroq
from tools.tavily_search import search

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def participant_agent(state):
    participants = state["participants"]

    insights = {}

    for person in participants:
        data = search(f"{person} professional background role")

        prompt = f"""
        Analyze this person:
        {data}

        Provide:
        - Role
        - Background
        - Likely priorities in a meeting
        """

        insights[person] = llm.invoke(prompt).content

    return {"participant_info": insights}