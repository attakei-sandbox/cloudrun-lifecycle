"""ASGI application endpoint module.
"""
import logging

from fastapi import FastAPI


logger = logging.getLogger(__name__)
app = FastAPI()


@app.on_event("startup")
async def _startup():
    """ASGI application configuration by environments
    """
    pass
