import yaml
import os

ABSPATH = os.path.dirname(os.path.abspath(__file__))
yaml_path = f"{ABSPATH}/../../config.yaml"

config = {}

with open(yaml_path) as f:
    config = yaml.safe_load(f)

    if "includes" in config:
        for path in config["includes"]:
            with open(f"{ABSPATH}/../../{path}") as f:
                tmp = yaml.safe_load(f)
                config.update(**tmp)
        del config["includes"]