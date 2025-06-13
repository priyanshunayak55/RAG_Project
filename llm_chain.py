from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
# from langchain_openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

def get_llm(provider="local"):
    # if provider == "openai":
    #     # OpenAI key is picked from environment variable OPENAI_API_KEY
    #     return OpenAI()
    if provider == "local":
        # Uses Ollama running locally with the "mistral" model
        return Ollama(model="granite3.2:8b")
    else:
        raise ValueError("Unsupported provider: choose 'local' or 'openai'.")

def run_llm(prompt: str, provider="local"):
    # You can adjust the prompt template as needed
    template = PromptTemplate.from_template("Answer the following:\n{question}")
    llm = get_llm(provider)
    chain = LLMChain(llm=llm, prompt=template)
    return chain.run(question=prompt)