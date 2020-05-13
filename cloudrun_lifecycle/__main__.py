"""Module endpoint.

- Merge CLI arguments and dotfile for application environment
- Run service as uvicorn application with env-file
"""
from .cli.run_server import main


main()
