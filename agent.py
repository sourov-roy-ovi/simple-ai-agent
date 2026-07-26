from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END

#========================================
# 1. GRAPH STATE DEFINITION
#========================================
class AgentState(TypedDict):
    """ Defines the schema fot the aget's shared memory state """
    messages: List[Union[HumanMessage, AIMessage]]
    