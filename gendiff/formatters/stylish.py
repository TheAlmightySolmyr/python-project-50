def form_val(value, depth):
    if isinstance(value, dict):
        indent = '    '
        lines = []
        for key, val in value.items():
            lines.append(f"{indent * (depth + 1)}{key}: {form_val(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + indent * depth + "}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_stylish(diff_tree, depth=0):
    indent = '    '
    lines = []

    for node in diff_tree:
        if node.type == 'added':
            lines.append(f"{indent * depth}+ {node.key}: {form_val(node.value, depth)}")
        elif node.type == 'removed':
            lines.append(f"{indent * depth}- {node.key}: {form_val(node.value, depth)}")
        elif node.type == 'changed':
            old_val, new_val = node.value
            lines.append(f"{indent * depth}- {node.key}: {form_val(old_val, depth)}")
            lines.append(f"{indent * depth}+ {node.key}: {form_val(new_val, depth)}")
        elif node.type == 'unchanged':
            lines.append(f"{indent * depth}  {node.key}: {form_val(node.value, depth)}")
        elif node.type == 'nested':
            lines.append(f"{indent * depth}  {node.key}: {{")
            lines.append(format_stylish(node.children, depth + 1))
            lines.append(f"{indent * depth}  }}")

    return '\n'.join(lines)