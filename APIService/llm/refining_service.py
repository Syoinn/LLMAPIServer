import re
import json
from .model_service import load_azure_llm, load_zhipu_llm
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from ..models.response_model import RefiningResponse
from ..templates.refining_template import POLISH_TEMPLATE

async def refining(text: str, style: str):
    model = load_zhipu_llm()
    parser = StrOutputParser()
    template = POLISH_TEMPLATE
    prompt = PromptTemplate.from_template(template)
    chain = prompt | model | parser
    response = await chain.ainvoke({"text": text, "style": style, "schema": RefiningResponse.model_config["json_schema_extra"]})
    processed_response = re.sub(r'^.*?```json(.*?)```.*$', r'\1', response, flags=re.DOTALL).strip()
    processed_response = processed_response.replace("\'", "\"")
    return json.loads(processed_response)
