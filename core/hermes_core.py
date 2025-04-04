import logging
from .hermes_loader import load_hulk
from .hermes_router import route_task
from utils.hermes_log import setup_logger

def process_task(task_name: str):
    """
    Main function to process a given task.
    Loads the hulk configuration, routes the task, and logs the activity.
    """
    setup_logger()
    logger = logging.getLogger(__name__)
    logger.info(f"Starting to process task: {task_name}")

    hulk_config = load_hulk()
    if not hulk_config:
        logger.error("Failed to load hulk configuration.")
        return

    task_result = route_task(task_name, hulk_config)

    logger.info(f"Task {task_name} processed with result: {task_result}")
    return task_result