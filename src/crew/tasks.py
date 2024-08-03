from crewai import Task

from crew import agents

code_generation_and_execution_task = Task(
    description="""Answer the provided prompt, generating Python code as needed, if any.
        Prompt: {base_prompt}""",
    expected_output="""Answer to the following prompt, using the same language as used in the prompt.
        Prompt: {base_prompt}""",
    agent=agents.software_engineer_agent,
)

code_generation_task = Task(
    description="""Generate Python code based on the given requirements and constraints.
        The code should be correct, clean, and follow the best practices and standards of Python development.
        The code should not rely on external libraries other than the ones currently installed.
        Consider the current libraries as matplotlib, langchain, crewai, flask, scikit-learn and sqlalchemy.
        The final result should contain only the code, without any explanation or formatting, without even markdown notation.""",
    expected_output="""Correct, clean Python code that follows the best practices and standards of Python development.""",
    agent=agents.code_generator_agent,
)

code_review_task = Task(
    description="""Evaluate Python code based on the given requirements and assess its quality and correctness.
        Ensure the code can be successfully executed, has no logic or syntax errors, is clean, and follows the best practices and standards.
        The review should focus on the correctness, readability, and adherence to the prompt requirements.
        Validate if no variable is used without being defined, including inside lambdas, and if the code is free of unused imports.
        The generated code should never include a library that is not currently installed.
        Code generated should contain only the code, without any explanation or formatting, without even markdown notation.""",
    expected_output="""Correct, clean Python code that follows the best practices and standards of Python development.""",
    agent=agents.code_reviewer_agent,
)

data_analysis_task = Task(
    description="""Analyse data from the provided source and get the results in a meaningful format.
        Consider the data source as informed in the provided prompt.
        Answer the provided prompt, generating Python code as needed, if any.
        Prompt: {base_prompt}""",
    expected_output="""Answer to the following prompt, using the same language as used in the prompt.
        Prompt: {base_prompt}""",
    agent=agents.data_analyst_agent,
)
