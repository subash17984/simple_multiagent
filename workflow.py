from agents.manager import project_manager
from agents.developer import developer
from agents.reviewer import reviewer
from agents.tester import tester
from agents.documentation import documentation

async def test(code):

    return await tester.run(
        task=f"""
Write pytest tests for this code.

{code}
"""
    )
    

MAX_REVISIONS = 2


class DevelopmentWorkflow:
    async def create_plan(self, project):
        return await project_manager.run(task=project)
    
    async def develop(self, plan):
        return await developer.run(
            task=f"""Implement the following software.
            
            project plan: {plan}
            
            """
        )
    async def review_code(self, code):
        return await reviewer.run(
            task=f"""
            Review this Implementation.
            {code}
            """
        )
        
    async def revise_code(self, code, review):
        return await developer.run(
            task=f"""
            The reviewer found these issues.
            
            Review:
            {review}
            
            Please improve the implementation.
            
            Original Code.
            {code}
            """
        )
        
    async def test(self, code):
        return await tester.run(
            task=f"""
            Write pytest tests for this code.
            
            {code}
            """
        )
    async def generate_documentation(
            self,
            project,
            code,
            tests
        ):

            return await documentation.run(
                task=f"""
        Project:

        {project}

        Implementation:

        {code}

        Tests:

        {tests}

        Write a professional README.md.
        """
            )
            
    async def generate_requirements(
            self,
            code
        ):

            return await documentation.run(
                task=f"""
        Analyze this Python project.

        Return only the requirements.txt content.

        Code:

        {code}
        """
            )
    async def run(self, project):
        
        print("Creating plan....")
        plan= await self.create_plan(project)
        
        print("Developing....")
        code=await self.develop(plan)
        
        approved=False
        revision=0
        
        while revision<MAX_REVISIONS:
            
            print(f"\nReview Round {revision + 1}")
            
            review=await self.review_code(code)
            
            print(review)
            
            if "APPROVED" in str(review):
                approved=True
                break
            
            print("Reviewer requested changes...")
            
            code = await self.revise_code(code, review)
            
            revision+=1
            
        if approved:
            print("\nGenerating tests...")
            tests=await self.test(code)
            
        else:
            tests="Testing skipped because the code was not approved."
            
        docs = await self.generate_documentation(
            project,
            code,
            tests
        )
        return{
            "plan": plan,

            "code": code,

            "review": review,

            "approved": approved,

            "revisions": revision,

            "tests": tests,
            
            "docs": docs,

        }