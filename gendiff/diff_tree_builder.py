from gendiff.diff_node import (
    AddedNode,
    ChangedNode,
    NestedNode,
    RemovedNode,
    UnchangedNode,
)


def build_diff_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff_tree = []

    for key in keys:
        if key not in data2:
            diff_tree.append(RemovedNode(key, value=data1[key]))
        elif key not in data1:
            diff_tree.append(AddedNode(key, value=data2[key]))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            diff_tree.append(NestedNode(key, children=children))
        elif data1[key] != data2[key]:
            diff_tree.append(
                ChangedNode(key, old_value=data1[key], new_value=data2[key])
            )
        else:
            diff_tree.append(UnchangedNode(key, value=data1[key]))

    return diff_tree