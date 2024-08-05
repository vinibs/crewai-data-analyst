import os

from dotenv import find_dotenv, load_dotenv

from crew import crews

load_dotenv(find_dotenv())


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


def data_anylisis_from_db():
    db_credentials = {
        "type": os.getenv("DB_TYPE"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    }

    base_prompt = (
        "Analyse the data from the database and provide a insights on where to explore to increase my selling numbers of motorcycle parts."
        f"The database credentials are as follows: {str(db_credentials)}."
        "Connect to the database and explore the data to find the insights as needed."
    )
    crew = crews.data_analysis_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    return result


def data_anylisis_from_data():
    base_prompt = (
        "Analyse the following data and provide a insights on where to explore to increase my selling numbers of motorcycle parts."
        "Data:"
        """
        Total Sales: 16871906.1971
        Average Sale Price: 59.20135128081329
        Top Customers:
        CLIENTE
        151467    874314.8672
        150132    610319.1386
        150625    346462.8396
        150682    334230.7831
        150551    304687.8754
        151423    287223.3100
        152131    269582.3100
        150453    265137.5099
        150251    253112.9621
        150944    243412.7202
        Name: VENDA TOTAL, dtype: float64
        Quantity Sold Analysis:
            QUANTIDADE COMRPADA  COUNT
        16                    2  14132
        24                   10  12013
        15                    1  10627
        19                    5  10605
        17                    3   7318
        34                   20   4603
        18                    4   4539
        20                    6   2954
        43                   30   1710
        57                   50   1255
        """
    )
    crew = crews.data_analysis_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    return result


def data_anylisis_from_db_portuguese():
    db_credentials = {
        "type": os.getenv("DB_TYPE"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_DATABASE"),
    }

    base_prompt = (
        "Analise os dados do banco de dados e forneça insights sobre onde explorar para aumentar meus números de venda de peças de motocicleta."
        f"As credenciais do banco de dados são as seguintes: {str(db_credentials)}."
        "Conecte-se ao banco de dados e explore os dados para encontrar os insights conforme necessário."
    )
    crew = crews.data_analysis_crew
    result = crew.kickoff(inputs={"base_prompt": base_prompt})
    return result


def main():
    # result = generate_code_only()
    # result = code_executioner()
    # result = data_anylisis_from_db()
    result = data_anylisis_from_db_portuguese()
    # result = data_anylisis_from_data()
    print(result)


if __name__ == "__main__":
    main()
