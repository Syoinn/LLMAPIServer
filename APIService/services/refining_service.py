from APIService.llm.language_model import load_azure_llm, load_zhipu_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from APIService.models.response_model import RefiningResponse
from refining_template import POLISH_TEMPLATE, EXPAND_TEMPLATE, SHORTEN_TEMPLATE, CONTINUE_TEMPLATE, \
    INSPIRATION_TEMPLATE
from typing import Dict, List

FUNC_DICT = {"polish": POLISH_TEMPLATE, "expand": EXPAND_TEMPLATE, "shorten": SHORTEN_TEMPLATE,
             "continue": CONTINUE_TEMPLATE, "inspiration": INSPIRATION_TEMPLATE}


async def refining(text: str, style: str, func: str) -> Dict[str, List[str]]:
    model = load_zhipu_llm()
    parser = StrOutputParser()
    if func not in FUNC_DICT:
        raise ValueError(f"Invalid function name: {func}")
    template = FUNC_DICT[func]

    prompt = PromptTemplate.from_template(template).partial()
    chain = prompt | model | parser
    response = await chain.ainvoke({
        "text": text,
        "style": style,
        "format_instructions": RefiningResponse.model_config["json_schema_extra"]
    })
    processed_response = RefiningResponse.from_raw_response(response)
    return processed_response.dict()
