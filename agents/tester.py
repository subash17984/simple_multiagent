from autogen_agentchat.agents import AssistantAgent
from config import model_client

tester = AssistantAgent(
    name="tester",
    model_client=model_client,
    system_message="""
You are a Senior QA Engineer.

Responsibilities:

- Review the implementation.
- Identify edge cases.
- Write pytest unit tests.
- Explain what each test verifies.

Only generate tests.
Do not modify the implementation.
"""
)