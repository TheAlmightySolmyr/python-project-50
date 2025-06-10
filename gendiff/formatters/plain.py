from gendiff.diff_node import (
    AddedNode,
    ChangedNode,
    NestedNode,
    RemovedNode,
)

REM_TEMPL = "Property '{}' was removed"
UPD_TEMPL = "Property '{}' was updated. From {} to {}"
ADD_TEMPL = "Property '{}' was added with value: {}"


def format_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        cur_pth = f"{path}.{node.key}" if path else node.key

        if isinstance(node, AddedNode):
            lines.append(ADD_TEMPL.format(cur_pth, format_value(node.value)))
        elif isinstance(node, RemovedNode):
            lines.append(REM_TEMPL.format(cur_pth))
        elif isinstance(node, ChangedNode):
            old_val = format_value(node.old_value)
            new_val = format_value(node.new_value)
            lines.append(UPD_TEMPL.format(cur_pth, old_val, new_val))
        elif isinstance(node, NestedNode):
            lines.append(format_plain(node.children, cur_pth))

    return '\n'.join(lines)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
