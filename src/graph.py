from langgraph.graph import StateGraph, END
from langchain_core.messages import SystemMessage, HumanMessage
from src.state import ResearchState
from agents.runner import executor_node
from src.agents import get_researcher, get_designer, get_coder, get_reviewer, get_benchmarker

def create_pipeline(llm):
    print("🔄 Building Master Pipeline (Stable & Modularized)...")
    
    # Initialize agents
    researcher_agent = get_researcher(llm)
    designer_agent = get_designer(llm)
    coder_agent = get_coder(llm)
    reviewer_agent = get_reviewer(llm)
    benchmarker_agent = get_benchmarker(llm)

    # 1. SPECIALIZED NODE FUNCTIONS
    def run_researcher(state):
        print("\n[STEP 1] RESEARCHER starting...")
        res = researcher_agent.invoke({"messages": state["messages"]})
        return {"messages": [res["messages"][-1]]}

    def run_designer(state):
        print("[STEP 2] DESIGNER starting...")
        prompt = [SystemMessage(content="Design the 'NormalFloat4Converter' class structure (quantize/dequantize).")] + state["messages"]
        res = llm.invoke(prompt)
        return {"messages": [res]}

    def run_coder(state):
        print("[STEP 3] CODER starting...")
        res = coder_agent.invoke({"messages": state["messages"]})
        return {"messages": [res["messages"][-1]]}

    def run_reviewer(state):
        print("[STEP 4] REVIEWER starting...")
        prompt = [SystemMessage(content="Audit the code. If perfect, say 'LGTM'. If not, explain errors.")] + state["messages"]
        res = llm.invoke(prompt)
        return {"messages": [res]}

    def run_benchmarker(state):
        print("[STEP 5] BENCHMARKER starting...")
        res = benchmarker_agent.invoke({"messages": state["messages"]})
        print("✅ TASK FINISHED.")
        return {"messages": [res["messages"][-1]]}

    # 2. ROUTING LOGIC
    def verify_review_final(state):
        lc = state["messages"][-1].content.upper()
        if "LGTM" in lc or "LOOKS GOOD" in lc:
            print(">>> Review Success -> Executor")
            return "executor"
        print(">>> Review Failed -> Coder")
        return "coder"

    def verify_execution_final(state):
        last_msg = state["messages"][-1].content.upper()
        if "SUCCESS" in last_msg and "FAILED" not in last_msg:
            print(">>> Execution Success -> Benchmarker")
            return "benchmarker"
        print(">>> Execution Failed -> Coder")
        return "coder"

    # 3. GRAPH ASSEMBLY
    builder = StateGraph(ResearchState)
    builder.add_node("researcher", run_researcher)
    builder.add_node("designer", run_designer)
    builder.add_node("coder", run_coder)
    builder.add_node("reviewer", run_reviewer)
    builder.add_node("executor", executor_node) 
    builder.add_node("benchmarker", run_benchmarker)

    builder.set_entry_point("researcher")
    builder.add_edge("researcher", "designer")
    builder.add_edge("designer", "coder")
    builder.add_edge("coder", "reviewer")
    builder.add_conditional_edges("reviewer", verify_review_final)
    builder.add_conditional_edges("executor", verify_execution_final)
    builder.add_edge("benchmarker", END)

    return builder.compile()
