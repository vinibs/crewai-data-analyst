import os

from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())


def load_bool_env(key: str, default: bool = False) -> bool:
    value = os.getenv(key, str(default))
    if value.lower() in ["true", "True", "1", "yes", "y"]:
        return True
    return False


def create_custom_llm(
    openai_api_key: str = None, openai_model: str = None
) -> ChatOpenAI:
    default_model = os.environ.get("OPENAI_MODEL_NAME", "gpt-4o-mini")
    default_openai_key = os.environ.get("OPENAI_API_KEY", None)

    model_to_use = openai_model if openai_model else default_model
    key_to_use = openai_api_key if openai_api_key else default_openai_key

    return ChatOpenAI(model=model_to_use, temperature=0, openai_api_key=key_to_use)
