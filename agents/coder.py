# agents/coder.py
from deepagents import create_deep_agent

def get_coder(llm, tools):
    """Factory function for the Lead Programmer (Coder)."""
    return create_deep_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are the Lead Programmer for DeepForge. "
            "Your goal is to implement the Architecture Designer's specification. "
            "1. Write complete, well-documented Python code. "
            "2. Include a 'main' block or test case to verify the implementation. "
            "3. Ensure you follow research paper naming conventions for variables. "
            "Output ONLY the Python code inside a markdown block."
        )
    )
