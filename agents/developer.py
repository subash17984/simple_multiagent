from autogen_agentchat.agents import AssistantAgent
from config import model_client

from tools.file_tools import create_file

developer=AssistantAgent(
    name="developer",
    model_client=model_client,
    tools=[create_file],
    system_message="""You are a Python developer.

Whenever you generate code,
save it using create_file().
""",
)