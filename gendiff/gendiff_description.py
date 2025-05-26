import argparse
import json

from yaml import safe_load

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


def generate_diff(file1, file2):
    data1 = parse_file_type(file1)
    data2 = parse_file_type(file2)

    keys = sorted(set(data1.keys()).union(set(data2.keys())))

    diff = []
    for key in keys:
        if key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
        else:
            diff.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(diff) + "\n}"


def get_gendiff():
    prsr = argparse.ArgumentParser(description=DESCRIPTION)
    prsr.add_argument('first_file', help='path to the first file')
    prsr.add_argument('second_file', help='path to the second file')
    prsr.add_argument('-f', '--format', help=HELP_DESCR, default='text')
    args = prsr.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)