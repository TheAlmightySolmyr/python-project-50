from gendiff.formatters.form_json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import form_sty


def get_formatter(format_name):
    if format_name == 'stylish':
        return form_sty
    elif format_name == 'plain':
        return format_plain
    elif format_name == 'json':
        return format_json