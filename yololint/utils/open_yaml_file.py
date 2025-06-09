import yaml
import os

def open_yaml_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(os.path.join(file_path, 'data.yaml'), 'r') as f:
        data_config = yaml.safe_load(f)
        return data_config
