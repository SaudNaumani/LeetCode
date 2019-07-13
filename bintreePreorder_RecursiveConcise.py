def preorderTraversal(self, root: TreeNode) -> List[int]:
    return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
