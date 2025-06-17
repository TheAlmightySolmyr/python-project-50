from gendiff.diff_tree_builder import build_diff_tree
from gendiff.formatters import get_formatter
from gendiff.parsers import parse_file_type


def generate_diff(file1, file2, format_name='stylish'):
    data1 = parse_file_type(file1)
    data2 = parse_file_type(file2)
    diff_tree = build_diff_tree(data1, data2)
    formated = get_formatter(format_name)
    return formated(diff_tree)