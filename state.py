from typing import TypedDict, List, Dict

class MeetingState(TypedDict):
    title: str
    company: str
    participants: List[str]
    goal: str
    expected_outcome:str

    company_info: Dict
    participant_info: Dict
    industry_insights: Dict
    strategy: Dict
    brief: str