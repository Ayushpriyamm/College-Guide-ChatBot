from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages

class application_state(TypedDict):
    course:str
    conversation:Annotated[list,add_messages]
    query_type:str
    retrived_context:str
    