import yaml
import logging
import os

def load_hulk():
    """
    Loads the hulk configuration from the YAML file.
    """
    logger = logging.getLogger(__name__)
    config_path = "config/baldr_hulkort.yaml"
    try:
        with open(config_path, 'r') as file:
            hulk_config = yaml.safe_load(file)
            logger.info("Hulk configuration loaded successfully.")
            return hulk_config
    except FileNotFoundError:
        logger.error(f"Configuration file not found at {config_path}")
        return None
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        return None