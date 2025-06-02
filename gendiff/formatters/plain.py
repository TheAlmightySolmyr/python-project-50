ADDED = 'was added with value:'
FROM = 'was updated. From'
CV = '[complex value]'
P = 'Property'
T = ' to '


def format_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        current_path = f"{path}.{node.key}" if path else node.key

        if node.type == 'added':
            if isinstance(node.value, dict):
                lines.append(f"{P} '{current_path}' {ADDED} {CV}")
            else:
                lines.append(f"{P} '{current_path}' {ADDED} {frm_v(node.value)}")
        elif node.type == 'removed':
            lines.append(f"{P} '{current_path}' was removed")
        elif node.type == 'changed':
            old_val, new_val = node.value
            if isinstance(old_val, dict) or isinstance(new_val, dict):
                lines.append(f"{P} '{current_path}' {FROM} {CV}{T}{CV}")
            else:
                lines.append(f"{P} '{current_path}' {FROM} {frm_v(old_val)}{T}{frm_v(new_val)}")
        elif node.type == 'nested':
            lines.append(format_plain(node.children, current_path))

    return '\n'.join(lines)


def frm_v(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
