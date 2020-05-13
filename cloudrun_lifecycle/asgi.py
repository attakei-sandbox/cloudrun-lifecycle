"""ASGI application endpoint module.
"""
import os
import logging

import slackweb
from fastapi import FastAPI


Logger = logging.getLogger(__name__)
app = FastAPI()
slack = slackweb.Slack(url=os.environ["SLACK_WEBHOOK_URL"])


@app.on_event("startup")
async def _startup():
    """ASGI application configuration by environments
    """
    Logger.info("Start container")
    slack.notify(text="Start container")


@app.on_event("shutdown")
async def _shutdown():
    slack.notify(text="Shutdown container")
    Logger.info("Shutdown container")
