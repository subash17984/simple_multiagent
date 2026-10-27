from autogen_agentchat.agents import AssistantAgent
from config import model_client
from tools.file_tools import create_file
documentation= AssistantAgent(
    name="documentation",
    model_client=model_client,
    tools=[create_file],
    system_message="""
You are a Senior Technical Writer.

Responsibilities:

- Write professional README.md files.
- Explain installation.
- Explain usage.
- Describe project structure.
- List dependencies.
- Include example commands.

Return only Markdown.
"""
)