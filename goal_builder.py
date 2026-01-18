from models import JobRequest

def build_goal(user: JobRequest) -> str:
    skills_list = [s.strip() for s in user.skills.split(",")]
    skills_text = ", ".join(skills_list)

    return f"""
    Open the LinkedIn Android app.
    Navigate to the Jobs section.

    Search for the job role: "{user.target_role}"

    Apply filters:
        Experience level: {user.experience_years} years
        Location: {user.preferred_location}

    While viewing job listings:
        - Prioritize roles that mention these skills:
          {skills_text}

        - Open job descriptions
        - Collect:
            Job title
            Company name
            Location
        - Stop after top 5 relevant jobs

    Handle popups if they appear.
    Use human-like scrolling and delays.
    """
