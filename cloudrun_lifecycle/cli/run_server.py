"""Run uvicorn server with this application.
"""
import logging

import click
import uvicorn
from dotenv import find_dotenv


logger = logging.getLogger(__name__)


@click.command()
@click.option("-D", "--debug", is_flag=True, default=False, help="uvicorn debug/reload")
@click.option("-p", "--port", type=int, default=8080)
def main(debug, port):
    dotenv_path = find_dotenv() or None
    if dotenv_path:
        logger.info("Find .env file. Use it in application.")
    uvicorn.run(
        "cloudrun_lifecycle.asgi:app",
        host="0.0.0.0",
        port=port,
        debug=debug,
        reload=debug,
        env_file=dotenv_path,
    )
