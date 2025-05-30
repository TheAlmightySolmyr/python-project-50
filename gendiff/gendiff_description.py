import argparse
import json
from pathlib import Path

from plain import format_plain
from yaml import safe_load

from gendiff.diff_tree_builder import build_diff_tree
from gendiff.form_json import format_json
from gendiff.stylish import format_stylish

DESCRIPTION = 'Compares two configuration files and shows a difference.'
HELP_DESCR = 'set format of output'
ERROR = 'Unsupported file format'


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
        raise ValueError(f'{ERROR}: {file_path}')


def generate_diff(file1, file2, format_name='stylish'):
    try:
        data1 = parse_file_type(file1)
        data2 = parse_file_type(file2)
    except Exception as e:
        raise ValueError(f"Error parsing files: {e}")

    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return f"{{\n{format_stylish(diff_tree)}\n}}"
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f"{ERROR}: {format_name}")


def get_gendiff():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file', help='path to the first file')
    parser.add_argument('second_file', help='path to the second file')
    parser.add_argument(
        '-f', '--format',
        help=HELP_DESCR,
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )
    args = parser.parse_args()
    try:
        diff = generate_diff(args.first_file, args.second_file, args.format)
        print(diff)
    except Exception as e:
        print(f"Error: {e}")