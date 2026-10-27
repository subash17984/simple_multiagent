import asyncio

from agents.manager import project_manager
from agents.developer import developer
from agents.reviewer import reviewer
# from tools.file_tools import create_file
from agents.tester import tester
from workflow import DevelopmentWorkflow

async def create_plan(project):
    return await project_manager.run(task=project)

async def develop(plan):
    return await developer.run(task=f"""Implement the following project.
                               Project plan: {plan}""")
    
async def review(code):
    return await reviewer.run(task=f"""Review the following code.
                               Code: {code}""")
async def test(code):
    return await tester.run(task=f"""Write pytest tests for the following code.
                               Code: {code}""")
    
async def main():
    workflow = DevelopmentWorkflow()
     
    project = input("Enter your software idea: ")

    result = await workflow.run(project)
     
    print("\n" + "=" * 60)
    print("PROJECT PLAN")
    print("=" * 60)
    print(result["plan"])
    
    print("\n" + "=" * 60)
    print("FINAL IMPLEMENTATION")
    print("=" * 60)
    print(result["code"])
    
    print("\n" + "=" * 60)
    print("FINAL REVIEW")
    print("=" * 60)
    print(result["review"])
    
    print("\n" + "=" * 60)
    print("TESTS")
    print("=" * 60)
    print(result["tests"])
    
    print("\nApproved:", result["approved"])
    print("Revision Count:", result["revisions"])
    
asyncio.run(main())