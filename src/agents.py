from agents.retriever import get_researcher as researcher_factory
from agents.planner import get_designer as designer_factory
from agents.coder import get_coder as coder_factory
from agents.reader import get_reviewer as reviewer_factory
from agents.extractor import get_benchmarker as benchmarker_factory
from src.tools import research_tools, coding_tools, testing_tools

def get_researcher(llm):
    return researcher_factory(llm, research_tools)

def get_designer(llm):
    return designer_factory(llm)

def get_coder(llm):
    return coder_factory(llm, coding_tools)

def get_reviewer(llm):
    return reviewer_factory(llm)

def get_benchmarker(llm):
    return benchmarker_factory(llm, testing_tools)
