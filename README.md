# ⚒️ DeepForge: Research-to-Production AI Pipeline

DeepForge is an autonomous, multi-agent AI system designed to bridge the gap between complex academic research and executable production code. By leveraging a coordinated swarm of specialized agents, DeepForge can ingest research papers (PDFs), extract their mathematical core, design robust class structures, and implement verified, testable Python modules.

---

## 🚀 Key Features

### 🧠 Multi-Agent Orchestration
DeepForge utilizes a sophisticated **LangGraph** workflow to coordinate specialized agents, ensuring high-fidelity output and self-healing code:
*   **🔍 Researcher Agent:** Scans ArXiv, downloads PDFs, and extracts mathematical centroids and logic.
*   **🎨 Architect Designer:** Transforms raw math into clean, object-oriented class specifications.
*   **💻 Lead Programmer (Coder):** Implements the design into high-performance PyTorch/NumPy code.
*   **🛡️ Peer Reviewer:** Audits the implementation against the research logic for 100% accuracy.
*   **⚙️ Autonomous Executor:** Runs the generated code in a secure sandbox to verify MSE and runtime stability.
*   **📊 Lead Scientist (Benchmarker):** Generates performance reports and verifies production-readiness.

### 🔬 Technical Capabilities
*   **Native NF4 Support:** Specialized pipeline for 4-bit NormalFloat (NF4) quantization as seen in QLoRA.
*   **Self-Healing Logic:** Automated feedback loops where agents fix execution errors and reviewer critiques in real-time.
*   **Windows-Safe Tooling:** Customized ArXiv and PDF processing tools optimized for across-platform stability.
*   **Live Progress Tracking:** Real-time logging of agent states and decisions for full transparency.

---

## 🛠️ Tech Stack

*   **Logic Framework:** [LangGraph](https://python.langchain.com/docs/langgraph) & [LangChain](https://python.langchain.com/)
*   **Intelligence:** Google Gemini 2.0 Flash
*   **Scientific Tools:** PyMuPDF (fitz), ArXiv API, Tavily Search
*   **Computations & Modeling:** PyTorch, NumPy
*   **Project Management:** DevGuardian Agent Swarm

---

## 📦 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Edge-Explorer/deepforge.git
    cd deepforge
    ```

2.  **Install Dependencies:**
    DeepForge uses `uv` or `pip`:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**
    Create a `.env` file with the following keys:
    ```env
    GOOGLE_API_KEY=your_gemini_key
    TAVILY_API_KEY=your_tavily_key
    ```

---

## 📋 Usage: The "Grand Test"

To see DeepForge in action, open `notebooks/deep_agent_prototype.ipynb` and run the **Stable Grand Test** cell. It will execute a full research-to-code cycle for NF4 quantization:

```python
# Example Prompt
"RESEARCH & IMPLEMENT: 4-bit NormalFloat (NF4) quantization. Phase 1: Researcher find values. Phase 2: Designer plan class. Phase 3: Coder implement & test MSE."
```

---

## 🗺️ Project Structure

```text
DeepForge/
├── notebooks/          # Interactive Agent Prototypes
├── src/                # Verified, Production-Ready Implementations
├── data/               # Downloaded Scientific Papers (PDFs)
├── experiments/        # Performance Reports & Benchmarks
└── agents/             # Custom Agent Definitions & System Prompts
```

---

## ⚖️ License

MIT License. See [LICENSE](LICENSE) for more details.

---
*Created by the Karan Shelar*
