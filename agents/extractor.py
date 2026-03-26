# agents/extractor.py
from deepagents import create_deep_agent

def get_benchmarker(llm, tools):
    """Factory function for the Lead Experiment Scientist (Extractor)."""
    return create_deep_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are the Lead Experiment Scientist. "
            "Your goal is to verify the 'Efficiency' claims of the research paper. "
            "1. Write a script that imports the saved module. "
            "2. Calculate metrics: Number of trainable parameters, Memory footprint, or Throughput. "
            "3. Output an 'Experiment Report' summarizing the efficiency gains."
        )
    )
