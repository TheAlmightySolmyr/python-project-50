class ChangedNode:
    def __init__(self, key, old_value, new_value):
        self.old_value = old_value
        self.new_value = new_value
        self.key = key
        
    def to_dict(self):
        return {
            "type": "changed",
            "key": self.key,
            "old_value": self.old_value,
            "new_value": self.new_value
        }        
        

class AddedNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        
    def to_dict(self):
        return {
            "type": "added",
            "key": self.key,
            "value": self.value
        }


class RemovedNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key

    def to_dict(self):
        return {
            "type": "removed",
            "key": self.key,
        }


class UnchangedNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key

    def to_dict(self):
        return {
            "type": "unchanged",
            "key": self.key,
            "value": self.value
        }


class NestedNode:
    def __init__(self, key, children):
        self.children = children
        self.key = key
        
    def to_dict(self):
        return {
            "type": "nested",
            "key": self.key,
            "children": [child.to_dict() for child in self.children]
        }