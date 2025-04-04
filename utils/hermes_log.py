import logging
import os

def setup_logger():
    """
    Sets up the logger to log information to a file.
    """
    log_file_path = "logs/ai-communication.md"
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(filename=log_file_path, level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())  # Also print to console