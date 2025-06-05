import argparse

from gendiff.diff_tree_builder import build_diff_tree
from gendiff.formatters.form_json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import form_sty
from gendiff.parsers import parse_file_type

DESCRIPTION = 'Compares two configuration files and shows a difference.'
HELP_DESCR = 'set format of output'


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file_type(file1)
    data2 = parse_file_type(file2)
    diff_tree = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return form_sty(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
    elif format_name == 'json':
        return format_json(diff_tree)
    else:
        raise ValueError(f"Unsupported file format: {format_name}")


def main():
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
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()