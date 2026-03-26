import os
import arxiv
import fitz
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

# 1. Initialize the Python Runtime
repl = PythonREPL()

# 2. arXiv Search and Download Tool
@tool
def download_research_paper(query: str) -> str:
    """Searches arXiv for a paper, downloads the PDF to 'data/' folder, returns local path."""
    download_path = "data/"
    os.makedirs(download_path, exist_ok=True)
    client = arxiv.Client()
    search = arxiv.Search(query=query, max_results=1, sort_by=arxiv.SortCriterion.Relevance)
    try:
        results = list(client.results(search))
        if not results: return "No papers found."
        paper = results[0]
        clean_title = "".join([c if c.isalnum() or c==' ' else '' for c in paper.title])
        filename = f"{clean_title.replace(' ', '_')}.pdf"
        full_path = paper.download_pdf(dirpath=download_path, filename=filename)
        return f"Paper downloaded to: {full_path}"
    except Exception as e:
        return f"Error during download: {str(e)}"

# 3. PDF Reading Tool
@tool
def read_pdf_content(file_path: str) -> str:
    """Reads a PDF's text content given a file path."""
    try:
        doc = fitz.open(file_path)
        text = "".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

# 4. Web Search Tool
web_search = TavilySearchResults(k=3)

# 5. Executing Python Code Tool
@tool
def execute_python_code(code: str) -> str:
    """Executes Python code and returns output, or errors if they occur."""
    try:
        clean_code = code.replace("```python", "").replace("```", "")
        if "import numpy" not in clean_code and ("np." in clean_code or "numpy" in clean_code):
            clean_code = "import numpy as np\n" + clean_code
        if "import torch" not in clean_code and ("torch" in clean_code or "nn." in clean_code):
            clean_code = "import torch\nimport torch.nn as nn\n" + clean_code
            
        result = repl.run(clean_code)
        if "Error" in result or "Traceback" in result:
            return f"Execution Failed:\n{result}"
        return f"Execution Success:\n{result if result else 'Code ran with no output (Success).'}"
    except Exception as e:
        return f"Execution Failed:\n{str(e)}"

# 6. Save Code to Production Tool
@tool
def save_code_to_production(code: str, filename: str) -> str:
    """Saves verified code to the 'src/' directory."""
    try:
        os.makedirs("src", exist_ok=True)
        clean_code = code.replace("```python", "").replace("```", "")
        file_path = os.path.join("src", filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(clean_code)
        return f"Production-ready code saved to: {file_path}"
    except Exception as e:
        return f"Failed to save code: {str(e)}"

# 7. Collect tools
research_tools = [download_research_paper, read_pdf_content, web_search]
coding_tools = [execute_python_code, save_code_to_production]
testing_tools = [execute_python_code]
all_tools = research_tools + coding_tools
