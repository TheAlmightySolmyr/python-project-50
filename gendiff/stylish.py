def format_stylish(diff_tree, depth=0):
    indent = '    '
    lines = []

    for node in diff_tree:
        if node.type == 'added':
            lines.append(f"{indent * depth}+ {node.key}: {node.value}")
        elif node.type == 'removed':
            lines.append(f"{indent * depth}- {node.key}: {node.value}")
        elif node.type == 'changed':
            old_value, new_value = node.value
            lines.append(f"{indent * depth}- {node.key}: {old_value}")
            lines.append(f"{indent * depth}+ {node.key}: {new_value}")
        elif node.type == 'unchanged':
            lines.append(f"{indent * depth}  {node.key}: {node.value}")
        elif node.type == 'nested':
            lines.append(f"{indent * depth}  {node.key}: {{")
            lines.append(format_stylish(node.children, depth + 1))
            lines.append(f"{indent * depth}  }}")

    return '\n'.join(lines)