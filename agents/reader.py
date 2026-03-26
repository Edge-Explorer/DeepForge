# agents/reader.py
from deepagents import create_deep_agent

def get_reviewer(llm, tools=None):
    """Factory function for the Peer Reviewer (Reader)."""
    return create_deep_agent(
        model=llm,
        tools=tools if tools else [],
        system_prompt=(
            "You are the Peer Reviewer. "
            "Your job is to audit the generated code against the original research logic. "
            "1. Check if the mathematical formulas match the paper. "
            "2. Look for missing initialization steps (e.g., zero-init for weights). "
            "3. Verify if variable names match the paper's notation. "
            "Output a 'Review Report'. If the code is perfect, say 'LGTM' (Looks Good To Me). "
            "If there are errors, explain them clearly so the Coder can fix them."
        )
    )
