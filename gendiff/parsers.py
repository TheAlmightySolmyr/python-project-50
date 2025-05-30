import json
from pathlib import Path

from yaml import safe_load


def parse_file_type(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if file_path.suffix == '.json':
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.suffix in ('.yml', '.yaml'):
        with open(file_path, 'r') as f:
            return safe_load(f)
    else:
        raise ValueError(f'Unsupported file format: {file_path}')