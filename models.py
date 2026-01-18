from pydantic import BaseModel

class JobRequest(BaseModel):
    target_role: str
    skills: str                 # comma-separated from UI
    experience_years: int
    preferred_location: str
