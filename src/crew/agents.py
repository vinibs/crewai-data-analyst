import logging

from crewai import Agent

from utils import create_custom_llm, load_bool_env

logger = logging.getLogger(__name__)

_max_agent_iterations = 5
_verbose = load_bool_env("VERBOSE_MODE", True)
_llm = create_custom_llm()

code_generator_agent = Agent(
    role="Software Engineer",
    goal="""Generate correct, clean Python code, following the best practices and standards.
        No explanation is needed. Only the final code is required.
        The resulting code should respect the following prompt request:
        {base_prompt}""",
    backstory="""You are a senior Software Engineer with 10+ years of experience in Python development.
        You have worked on various projects and have a deep understanding of the best practices and standards in Python development.""",
    allow_delegation=False,
    max_iter=_max_agent_iterations,
    llm=_llm,
    verbose=_verbose,
)

code_reviewer_agent = Agent(
    role="Code Reviewer",
    goal="""Review the generated code and provide feedback to the Software Engineer,
        ensuring the code is correct, runnable and that it follows the best practices and standards.
        Ensure the response only includes the code and no explanation.
        The resulting code should respect the following prompt request:
        {base_prompt}""",
    backstory="""You are a Senior Software Engineer and Code Reviewer with experience in reviewing Python code.
        You have a keen eye for detail and can identify issues in the code quickly.
        You also have a great skill for providing feedbacks to make the resulting code more concise and clean.""",
    allow_delegation=False,
    max_iter=_max_agent_iterations,
    llm=_llm,
    verbose=_verbose,
)


software_engineer_agent = Agent(
    role="Software Engineer",
    goal="""Generate correct, clean Python code, following the best practices and standards.
        Execute the code to ensure it works as expected.
        Output the result of the code execution, providing explanations on what was done and the data returned.
        The result should answer to the following prompt request:
        {base_prompt}""",
    backstory="""You are a senior Software Engineer with 10+ years of experience in Python development.
        You have worked on various projects and have a deep understanding of the best practices and standards in Python development.""",
    allow_delegation=False,
    allow_code_execution=True,
    max_iter=_max_agent_iterations,
    llm=_llm,
    verbose=_verbose,
)
