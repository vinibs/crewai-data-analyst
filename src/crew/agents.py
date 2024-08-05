import logging

from crewai import Agent

from crew.tools import CustomCodeInterpreterTool
from utils import create_custom_llm, load_bool_env

logger = logging.getLogger(__name__)

_max_agent_iterations = 15
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


data_analyst_agent = Agent(
    role="Data Analyst",
    goal="""Assess the data available for analysis and answer the provided prompt request.
        Use your expertise in data analysis through Python to generate and execute code as needed to get and process the data.

        Never assume a database structure or table name if it's not explicitly provided in the prompt.
        In this case, firstly fetch the database to understand its structure, for both the table and column names.
        Always use the credentials provided in the prompt to connect to the database, when a connection is needed.
        When connecting to the database, always close the connection at the end of the code.
        If no database access is provided, but the data is available, use the data provided to answer the prompt.
        If dealing with static data, use it as is, without any modifications. Analyse it and answer the prompt directly.
        Always wrap column names in double quotes, escaped with three backslashes (\\\\\\"), when using them in SQL queries also wrapped in double quotes.
        Always escape double quotes with a backslash (\\").
        Always escape percent signs (%) with a backslash (\\%).
        Prioritize using SQLAlchemy to connect to a database when necessary.
        Always wrap SQL code inside a text() function from SQLAlchemy to prevent errors.
        Never simulate any data. If no database access or data is provided, return a message stating that you were unable to access the data.
        If a connection to the database is needed, ensure to close the connection after the data is fetched.
        Never assume any variable or function is already defined when generating code.
        Consider every code generation as a new execution in a clean environment.
        Always import required libraries and define all variables and functions needed.
        When connecting to a database, never, in any circumstance, use any operation other than SELECT.
        Your code should never run any operation in the host system or that modifies the database.
        Always print the result in the end of the code generated.

        If the generated code already prints the result, answer with it directly instead of trying a new execution.
        The result should answer to the following prompt request, in the same language it was asked:
        {base_prompt}""",
    backstory="""You are a senior Data Analyst and Python Developer with 10+ years of experience in data analysis using Python.""",
    allow_delegation=False,
    tools=[CustomCodeInterpreterTool(run_in_docker=False)],
    max_iter=_max_agent_iterations,
    llm=_llm,
    verbose=_verbose,
)
