import asyncio
from fastapi import FastAPI
from models import JobRequest
from goal_builder import build_goal
from agent_runner import run_agent

app = FastAPI()

@app.post("/search-jobs")
async def search_jobs(request: JobRequest):
    goal = build_goal(request)

    # Non-blocking execution
    asyncio.create_task(run_agent(goal))

    return {
        "status": "started",
        "message": "LinkedIn job search automation started"
    }
