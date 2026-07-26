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

#========================================
# 2. LLM INITIALIZATION
#========================================
# Using Qwen 2.5 local instance via Ollma with deterministic sampling
llm = ChatOllama(
    model="qwen2.5:14b",
    temperature=0
)

#========================================
# 3. GRAPH NODES (BUSINESS LOGIC)
#========================================
def process(state: AgentState) -> AgentState:
    """ Node to process incoming user messages and return the model """
    response = llm.invoke(state["messages"])
    print(f"\AI: {response.content}")
    return{
        'messages':state['messages'] + [AIMessage(content=response.content)]
    }