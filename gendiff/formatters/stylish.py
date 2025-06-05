def form_val(value, depth):
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {form_val(val, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * depth + '}'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def format_stylish(diff_tree, depth=0):
    indent = '    ' * depth
    lines = []
    
    for node in diff_tree:
        key = node.key
        node_type = node.type
        
        if node_type == 'nested':
            lines.append(f"{indent}    {key}: {format_stylish(node.children, depth + 1)}")
        elif node_type == 'changed':
            old_val = form_val(node.value[0], depth + 1)
            new_val = form_val(node.value[1], depth + 1)
            lines.append(f"{indent}  - {key}: {old_val}")
            lines.append(f"{indent}  + {key}: {new_val}")
        elif node_type == 'added':
            lines.append(f"{indent}  + {key}: {form_val(node.value, depth + 1)}")
        elif node_type == 'removed':
            lines.append(f"{indent}  - {key}: {form_val(node.value, depth + 1)}")
        else:  # unchanged
            lines.append(f"{indent}    {key}: {form_val(node.value, depth + 1)}")
    
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'