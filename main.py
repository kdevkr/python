import os

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Load environment
dotenv_file = find_dotenv()
print(f"Load env from {dotenv_file}")
load_dotenv(dotenv_file)
PORT = os.getenv('PORT')

scheduler = AsyncIOScheduler(timezone=os.getenv('TZ'))


@scheduler.scheduled_job('interval', minutes=1)
def publish_message():
    print("publish!!")


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def index():
    return "OK"


if __name__ == "__main__":
    # FastAPI is an ASGI web framework.
    uvicorn.run(app=app, host="0.0.0.0", port=int(PORT))
