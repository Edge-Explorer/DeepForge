# agents/retriever.py
from deepagents import create_deep_agent

def get_researcher(llm, tools):
    """Factory function for the Researcher (Retriever) Agent."""
    return create_deep_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are the Paper-to-Production Analyzer. "
            "Your mission is to find research papers and extract their implementation core. "
            "Step 1: Use 'download_research_paper' to get the PDF. "
            "Step 2: Use 'read_pdf_content' to understand the math and logic. "
            "Step 3: Output a structured explanation of the algorithm, variables, and pseudocode."
        )
    )
