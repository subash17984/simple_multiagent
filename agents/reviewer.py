from autogen_agentchat.agents import AssistantAgent
from config import model_client

reviewer=AssistantAgent(
    name="reviewer",
    model_client=model_client,
    system_message="""
You are a Senior code reviewer.

Review the submitted code.

If the code is good enough to continue,
start your response with:

APPROVED

Otherwise start your response with:

CHANGES_REQUIRED

Then explain what needs to be fixed.

Be specific.
"""
)