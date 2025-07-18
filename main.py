import os

import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

# Load environment
dotenv_file = find_dotenv()
print(f"Load env from {dotenv_file}")
load_dotenv(dotenv_file)
PORT = os.getenv('PORT')


def publish_message():
    print("publish!!")


scheduler = BackgroundScheduler(daemon=True, timezone=os.getenv('TZ'))
scheduler.add_job(publish_message, 'interval', minutes=1)
scheduler.start()

app = FastAPI()


@app.get("/")
def index():
    return "OK"


if __name__ == "__main__":
    try:
        # FastAPI is an ASGI web framework.
        uvicorn.run(app=app, host="0.0.0.0", port=int(PORT))
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
