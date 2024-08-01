from crew import crews


def main():
    base_prompt = "Create a function to sum two numbers and return the result. The function should be named `sum_numbers` and should take two arguments, `a` and `b`. The function should return the sum of `a` and `b`."

    crew = crews.code_generation_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    print(result)


if __name__ == "__main__":
    main()
