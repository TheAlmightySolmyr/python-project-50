import json


def format_json(diff_tree):
    diff_list = [node.to_dict() for node in diff_tree]
    return json.dumps(diff_list, indent=2)
