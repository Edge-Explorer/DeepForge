# agents/planner.py
from deepagents import create_deep_agent

def get_designer(llm, tools=None):
    """Factory function for the Architect Designer (Planner) Agent."""
    return create_deep_agent(
        model=llm,
        tools=tools if tools else [],
        system_prompt=(
            "You are the Architecture Designer. "
            "Your goal is to take research findings and create a high-level Design Spec. "
            "1. Define the Python classes and methods needed. "
            "2. Specify the exact mathematical formulas for each method. "
            "3. Decide on the libraries to use (e.g., torch, numpy). "
            "Output ONLY the design specification, not the actual code yet."
        )
    )
