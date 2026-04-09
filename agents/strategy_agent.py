from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

def strategy_agent(state):
    prompt = f"""
    You are a strategic meeting advisor.

    Meeting Goal: {state['goal']}

    Company Info:
    {state['company_info']}

    Participant Info:
    {state['participant_info']}

    Industry Insights:
    {state['industry_insights']}
    
    Brief about meeting what we are aiming from this meeting:
    {state['expected_outcome']}

    Generate:
    - Meeting objectives
    - Key talking points
    - Smart questions to ask
    - Risks to prepare for
    """

    response = llm.invoke(prompt)

    return {"strategy": response.content}