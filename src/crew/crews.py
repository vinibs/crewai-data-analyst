from crewai import Crew

from crew import agents, tasks
from utils import create_custom_llm, load_bool_env

_verbose = load_bool_env("VERBOSE_MODE", True)
_llm = create_custom_llm()

code_generation_crew = Crew(
    agents=[agents.software_engineer_agent, agents.code_reviewer_agent],
    tasks=[tasks.code_generation_task, tasks.code_review_task],
    manager_llm=_llm,
    verbose=_verbose,
)
