from droidrun import DroidAgent, DroidrunConfig, AdbTools
from config import get_llm, get_agent_config

async def run_agent(goal: str):
    llm = get_llm()
    tools = AdbTools()

    config = DroidrunConfig(
        agent=get_agent_config()
    )

    agent = DroidAgent(
        goal=goal,
        llms=llm,
        tools=tools,
        config=config
    )

    await agent.run()
