def form_val(value, dpth):
    if isinstance(value, dict):
        ind = '    '
        lines = []
        for key, val in value.items():
            lines.append(f"{ind * (dpth + 1)}{key}: {form_val(val, dpth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + ind * dpth + "}"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_stylish(diff_tree, dpth=0):
    ind = '    '
    lines = []

    for n in diff_tree:
        if n.type == 'added':
            lines.append(f"{ind * dpth}+ {n.key}: {form_val(n.value, dpth)}")
        elif n.type == 'removed':
            lines.append(f"{ind * dpth}- {n.key}: {form_val(n.value, dpth)}")
        elif n.type == 'changed':
            ol_val, new_val = n.value
            lines.append(f"{ind * dpth}- {n.key}: {form_val(ol_val, dpth)}")
            lines.append(f"{ind * dpth}+ {n.key}: {form_val(new_val, dpth)}")
        elif n.type == 'unchanged':
            lines.append(f"{ind * dpth}  {n.key}: {form_val(n.value, dpth)}")
        elif n.type == 'nested':
            lines.append(f"{ind * dpth}  {n.key}: {{")
            lines.append(format_stylish(n.children, dpth + 1))
            lines.append(f"{ind * dpth}  }}")

    return '\n'.join(lines)