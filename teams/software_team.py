from autogen_agentchat.teams import RoundRobinGroupChat

from agents.manager import project_manager
from agents.developer import developer
from agents.reviewer import reviewer
from agents.tester import tester

software_team = RoundRobinGroupChat(
    participants=[
        project_manager,
        
        developer,
        
        reviewer,
        
        tester
    ]
)