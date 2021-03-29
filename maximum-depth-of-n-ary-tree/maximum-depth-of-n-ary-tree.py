class Solution:
    def __init__(self):
        self.max_depth = []
        
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        _max = 0
        for child in root.children:
            _max = max(_max, self.maxDepth(child))
        return _max + 1