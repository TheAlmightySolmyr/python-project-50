REM_TEMPL = "Property '{}' was removed"
UPD_TEMPL = "Property '{}' was updated. From {} to {}"
ADD_TEMPL = "Property '{}' was added with value: {}"

def format_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        cur_pth = f"{path}.{node.key}" if path else node.key

        if node.type == 'added':
            lines.append(ADD_TEMPL.format(cur_pth, frm_v(node.value)))
        elif node.type == 'removed':
            lines.append(REM_TEMPL.format(cur_pth))
        elif node.type == 'changed':
            old_val = frm_v(node.value[0])
            new_val = frm_v(node.value[1])
            lines.append(UPD_TEMPL.format(cur_pth, old_val, new_val))
        elif node.type == 'nested':
            lines.append(format_plain(node.children, cur_pth))

    return '\n'.join(lines)


def frm_v(value):
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
