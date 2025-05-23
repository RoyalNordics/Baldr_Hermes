# Loads Baldr's build ruleset

import yaml

def load_hulkort(path="baldr_hulkort.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)