from autogen_agentchat.agents import AssistantAgent
from config import model_client

project_manager=AssistantAgent(
    name="project_manager",
    model_client=model_client,
    system_message="""
You are an experienced software project manager.

Your responsibilities:
- Understand the user's request.
- Break the project into clear development tasks.
- Return the tasks as a numbered list.
Do not write any code.
""",
)