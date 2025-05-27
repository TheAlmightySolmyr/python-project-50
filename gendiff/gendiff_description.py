import argparse
import json

from yaml import safe_load

from gendiff.diff_tree_builder import build_diff_tree
from gendiff.stylish import format_stylish

DESCRIPTION = 'Compares two configuration files and shows a difference.'
HELP_DESCR = 'set format of output'
ERROR = 'Unsupported file format'


def parse_file_type(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r') as f:
            return safe_load(f)
    else:
        raise ValueError(f'{ERROR}: {file_path}')


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file_type(file1)
    data2 = parse_file_type(file2)

    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return f'{{\n{format_stylish(diff_tree)}\n}}'
    else:
        raise ValueError(f'{ERROR}: {format_name}')


def get_gendiff():
    prsr = argparse.ArgumentParser(description=DESCRIPTION)
    prsr.add_argument('first_file', help='path to the first file')
    prsr.add_argument('second_file', help='path to the second file')
    prsr.add_argument('-f', '--format', help=HELP_DESCR, default='stylish')
    args = prsr.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)