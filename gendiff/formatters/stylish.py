from gendiff.diff_node import (
    AddedNode,
    ChangedNode,
    NestedNode,
    RemovedNode,
)


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


def form_sty(diff_tree, dpth=0):
    indent = '    ' * dpth
    lines = []
    
    for n in diff_tree:
        key = n.key
        
        if isinstance(n, NestedNode):
            lines.append(f"{indent}    {key}: {form_sty(n.children, dpth + 1)}")
        elif isinstance(n, ChangedNode):
            old_val = form_val(n.old_value, dpth + 1)
            new_val = form_val(n.new_value, dpth + 1)
            lines.append(f"{indent}  - {key}: {old_val}")
            lines.append(f"{indent}  + {key}: {new_val}")
        elif isinstance(n, AddedNode):
            lines.append(f"{indent}  + {key}: {form_val(n.value, dpth + 1)}")
        elif isinstance(n, RemovedNode):
            lines.append(f"{indent}  - {key}: {form_val(n.value, dpth + 1)}")
        else:
            lines.append(f"{indent}    {key}: {form_val(n.value, dpth + 1)}")
    
    return '{\n' + '\n'.join(lines) + '\n' + indent + '}'