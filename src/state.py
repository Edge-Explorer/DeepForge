from typing import Annotated, List, TypedDict, Optional, Union
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class ResearchState(TypedDict):
    """The graph state for the DeepForge research-to-production pipeline."""
    messages: Annotated[list[BaseMessage], add_messages]
    paper_path: Optional[str]
    scientific_logic: Optional[str]
    implementation_code: Optional[str]
