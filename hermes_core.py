# Hermes Core - Baldr's primary AI builder coordinator

from hermes_loader import load_hulkort
from hermes_router import route_task
from hermes_log import log

def process_task(task_text):
    rules = load_hulkort()
    log("Task received", task_text)
    output = route_task(task_text, rules)
    log("Task processed", output)
    return output