from crew import crews


def generate_code_only():
    base_prompt = (
        "Create a function to sum two numbers and return the result. "
        "The function should be named `sum_numbers` and should take two arguments, "
        "`a` and `b`. The function should return the sum of `a` and `b`."
    )
    crew = crews.code_generation_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    return result


def code_executioner():
    base_prompt = (
        "Calculate the average of the numbers 5, 10, 15, 20, 25, 30, 35, 40, 45, 50. "
        "After calculating the average, round the result to the nearest integer and take its square root. "
        "Describe step by step the process you followed to calculate the final result. Also provide the final result."
    )
    crew = crews.code_processing_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    return result


def main():
    # result = generate_code_only()
    result = code_executioner()
    print(result)


if __name__ == "__main__":
    main()
