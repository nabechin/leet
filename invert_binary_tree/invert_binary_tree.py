class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = root.left if root.left else None
        root.left = root.right if root.right else None
        root.right = left
        self.invertTree(root.left if root else None)
        self.invertTree(root.right if root else None)
        return root