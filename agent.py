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
    print(f"\nAI: {response.content}")
    return{
        'messages':state['messages'] + [AIMessage(content=response.content)]
    }

#========================================
# 4. GRAPH ARCHITECTURE AND COMPILATION
#========================================
# Define the workflow topology
graph = StateGraph(AgentState)
graph.add_node("process", process)

# Route execution flow
graph.add_edge(START, "process")
graph.add_edge("process", END)

# Compile into and executable LangGraph runnable
agent = graph.compile()

#=========================================
# 5. APPLICATION RUNTIME (CLI CHAT LOOP)
#=========================================
conversation_history = []
while True:
    user_input = input("Enter: ")
    if user_input.lower() == "exit":
        break
    conversation_history.append(HumanMessage(content=user_input))
    
    # Invoke the graph execution with the current state
    result = agent.invoke({'messages':conversation_history})
    conversation_history = result['messages']

#==========================================
# 6. PERSISTENCE / LOGGING
#==========================================
# TOOO: Implement ans absolute path or dynamic naming to prevent file overwrites
with open("logging.txt", "w", encoding="utf-8") as file:
    file.write("Your conversation log: \n")
    
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    
    file.write("\n End of conversation")

print("Conversation successfully saved to loggin.txt")