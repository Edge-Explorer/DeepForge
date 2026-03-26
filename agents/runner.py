# agents/runner.py
from langchain_core.messages import HumanMessage
from src.tools import execute_python_code

def executor_node(state):
    """The node for running and verifying code in the LangGraph logic."""
    print("[EXECUTOR] Running code tests...")
    
    # Scan history for the most recent python code block
    code = None
    for msg in reversed(state["messages"]):
        if "```python" in msg.content:
            code = msg.content.split("```python")[1].split("```")[0]
            break
            
    if code:
        result = execute_python_code.invoke(code)
        return {"messages": [HumanMessage(content=f"EXECUTOR RESULTS:\n{result}")]}
        
    return {"messages": [HumanMessage(content="ERROR: No code block found in conversation history.")]}
