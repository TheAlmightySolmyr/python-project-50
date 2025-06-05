from gendiff.diff_node import DiffNode


def build_diff_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff_tree = []

    for key in keys:
        if key not in data2:
            diff_tree.append(DiffNode(key, 'removed', value=data1[key]))
        elif key not in data1:
            diff_tree.append(DiffNode(key, 'added', value=data2[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            diff_tree.append(DiffNode(key, 'nested', children=children))
        elif data1[key] != data2[key]:
            diff_tree.append(
                DiffNode(key, 'changed', value=(data1[key], data2[key]))
            )
        else:
            diff_tree.append(DiffNode(key, 'unchanged', value=data1[key]))

    return diff_tree