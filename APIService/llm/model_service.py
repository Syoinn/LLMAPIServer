from functools import lru_cache

from langchain_openai import AzureChatOpenAI
from langchain_community.chat_models import ChatZhipuAI


@lru_cache(maxsize=1)
def load_azure_llm() -> AzureChatOpenAI:
    """Load GPT 3.5 Model"""
    return AzureChatOpenAI(
        azure_deployment="gpt-35-turbo",
        openai_api_version="2024-05-01-preview",
        temperature=0.5,
    )

@lru_cache(maxsize=1)
def load_zhipu_llm() -> ChatZhipuAI:
    """Load Zhipu Model"""
    return ChatZhipuAI(
        model="glm-4-0520",
        temperature=0.5,
    )