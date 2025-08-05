from google.adk import Agent
from google.adk.tools import google_search

# Define server-side agent
root_agent = Agent(
    # Agent unique identifier
    name="facts_agent",
    
    # Large language model to use
    model="gemini-2.0-flash",
    
    # Agent functionality description
    description="Agent to give interesting facts.",
    
    # Agent behavior instructions
    instruction=(
        "You are a helpful agent who can provide interesting facts. "
        "Use Google Search to find accurate and up-to-date information. "
        "Always provide sources for your facts."
    ),
    
    # Available tools list
    tools=[google_search],
)