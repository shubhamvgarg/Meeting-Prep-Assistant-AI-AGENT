from langchain_core.tools import Tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search(query: str):
    response = client.search(query=query, search_depth="advanced")
    return response["results"]

tavily_tool = Tool(
    name="tavily_search",
    func=search,
    description="Search the web for recent and relevant information"
)