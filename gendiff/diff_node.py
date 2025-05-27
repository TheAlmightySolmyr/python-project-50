class DiffNode:
    def __init__(self, key, type, value=None, children=None):
        self.key = key
        self.type = type  # 'added', 'removed', 'changed', 'unchanged', 'nested'
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return (
            f"DiffNode(key={self.key}, type={self.type}, "
            f"value={self.value}, children={self.children})"
        )