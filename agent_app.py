# User → LLM → Response
# Use agents

from dotenv import load_dotenv
from pprint import pprint
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage

load_dotenv()

def simple_agent_call():
    agent = create_agent("gpt-5-nano")
    
    response = agent.invoke(
        {
            "messages":[
                HumanMessage(content="What's the capital of the Moon?")
            ]
        }
    )
    
    print("\n=== FULL RESPONSE ===")
    pprint(response)
    
    print("\n=== FINAL MESSAGE ===")
    print(response["messages"][-1].content)
    
def multi_turn_conversation():
    agent = create_agent("gpt-5-nano")
    
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content="What's the capital of the Monn?"),
                AIMessage(content="The capital of the Moon is Luna City."),
                HumanMessage(content="Interesting, tell me more about Luna City")
            ]
        }
    )
    
    print("\n=== MULTI TURN RESPONSE ===")
    pprint(response)
    
    print("\n=== FINAL MESSAGE ===")
    print(response["messages"][-1].content)

def stream_agent_call():
    agent = create_agent("gpt-5-nano")
    
    print("\n=== STREAM RESPONSE ===")
    for token, metadata in agent.stream(
        {"messages": [HumanMessage(content="Tell me all about Luna City, the capital of the Moon")]},
        stream_mode="messages"
    ):
        
        # token is a message chunk with token content
        # metadata contains which node produced the token
        if token.content:  # Check if there's actual content
            print(token.content, end="", flush=True)  # Print token


if __name__ == "__main__":
    print("\n-- SIMPLE AGENT ---")
    simple_agent_call()
    
    print("\n--- MULTI TURN ---")
    multi_turn_conversation()
    
    print("\n--- STREAM TURN ---")
    stream_agent_call()