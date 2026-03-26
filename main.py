from dotenv import load_dotenv
load_dotenv() # Load environment variables before any other imports that might use them

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from src.graph import create_pipeline

# 2. Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

# 3. Create the Pipeline
pipeline = create_pipeline(llm)

# 4. Define Initial Input
inputs = {
    "messages": [
        ("user", "IMPLEMENT NF4: Use these 16 centroids: [-1.0, -0.6961, -0.5250, -0.3949, -0.2844, -0.1847, -0.0910, 0.0, 0.0795, 0.1609, 0.2461, 0.3379, 0.4407, 0.5626, 0.7229, 1.0]. Implement the NormalFloat4Converter class and test MSE.")
    ]
}

config = {"configurable": {"thread_id": "modular-production-v1"}}

# 5. Execute Pipeline
print("🚀 INITIATING MODULARIZED TEST: Watch the clean node-by-node flow...\n")

for event in pipeline.stream(inputs, config):
    for node_name, output in event.items():
        print(f"\n{'='*20} [{node_name.upper()} COMPLETED] {'='*20}")
        if "messages" in output:
            print(output["messages"][-1].content)
