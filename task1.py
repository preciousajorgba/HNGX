from fastapi import FastAPI, Query
from datetime import datetime
from pytz import utc

app = FastAPI()

@app.get("/api")
async def get_info(
    slack_name: str = Query(..., title="Slack Name"),
    track: str = Query(..., title="Track"),
):
    # Get current day of the week
    current_day = datetime.now(utc).strftime('%A')

    # Get current UTC time
    current_utc_time = datetime.now(utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub file and repo URLs
    github_file_url = "https://github.com/preciousajorgba/HNGX/blob/main/task1.py"
    github_repo_url = "https://github.com/preciousajorgba/HNGX"

    # Response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return response_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
