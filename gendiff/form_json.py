import json


def format_json(diff_tree):
    def build_diff(node):
        if node.type == 'added':
            return {'type': 'added', 'key': node.key, 'value': node.value}
        elif node.type == 'removed':
            return {'type': 'removed', 'key': node.key}
        elif node.type == 'changed':
            old_value, new_value = node.value
            return {
                'type': 'changed',
                'key': node.key,
                'old_value': old_value,
                'new_value': new_value
            }
        elif node.type == 'unchanged':
            return {'type': 'unchanged', 'key': node.key, 'value': node.value}
        elif node.type == 'nested':
            return {
                'type': 'nested',
                'key': node.key,
                'children': [build_diff(child) for child in node.children]
            }

    diff_list = [build_diff(node) for node in diff_tree]
    return json.dumps(diff_list, indent=2)
