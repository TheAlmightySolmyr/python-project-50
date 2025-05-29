ADDED = 'was added with value:'
FROM = 'was updated. From'
CV = '[complex value]'
P = 'Property'
T = ' to '


def format_plain(diff_tree, path=""):
    lns = []

    for n in diff_tree:
        pth = f"{path}.{n.key}" if path else n.key

        if n.type == 'added':
            if isinstance(n.value, dict):
                lns.append(f"{P} '{pth}' {ADDED} {CV}")
            else:
                lns.append(f"{P} '{pth}' {ADDED} {frm_v(n.value)}")
        elif n.type == 'removed':
            lns.append(f"{P} '{pth}' was removed")
        elif n.type == 'changed':
            ol_v, n_v = n.value
            if isinstance(ol_v, dict) or isinstance(n_v, dict):
                lns.append(f"{P} '{pth}' {FROM} {CV} to {CV}")
            else:
                lns.append(f"{P} '{pth}' {FROM} {frm_v(ol_v)}{T}{frm_v(n_v)}")
        elif n.type == 'nested':
            lns.append(format_plain(n.children, pth))

    return '\n'.join(lns)


def frm_v(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)