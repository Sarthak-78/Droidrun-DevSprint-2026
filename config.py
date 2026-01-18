import os
from llama_index.llms.google_genai import GoogleGenAI
from droidrun import AgentConfig

def get_llm():
    return GoogleGenAI(
        api_key=os.environ["GOOGLE_API_KEY"],
        model="models/gemini-2.5-pro"
    )

def get_agent_config():
    return AgentConfig(
        max_steps=25,
        step_timeout=10,
        retry_on_failure=True
    )

