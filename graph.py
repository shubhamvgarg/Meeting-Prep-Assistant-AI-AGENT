from langgraph.graph import StateGraph, START, END
from state import MeetingState

from agents.company_agent import company_agent
from agents.participant_agent import participant_agent
from agents.industry_agent import industry_agent
from agents.strategy_agent import strategy_agent
from agents.brief_agent import brief_agent

def build_graph():

    graph = StateGraph(MeetingState)

    graph.add_node("company", company_agent)
    graph.add_node("participants", participant_agent)
    graph.add_node("industry", industry_agent)
    graph.add_node("strategy", strategy_agent)
    graph.add_node("brief", brief_agent)

    graph.set_entry_point("company")

    graph.add_edge(START, "company")
    graph.add_edge("company", "participants")
    graph.add_edge("participants", "industry")
    graph.add_edge("industry", "strategy")
    graph.add_edge("strategy", "brief")
    graph.add_edge("brief", END)

    return graph.compile()