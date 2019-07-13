def preorderRecursive(self, root: TreeNode, result: List[int]) -> List[int]:
    if (root is None):
        return
    result.append(root.val)
    self.preorderRecursive(root.left, result)
    self.preorderRecursive(root.right, result)
    return result
def preorderTraversal(self, root: TreeNode) -> List[int]:
    # preorder is root, left, right
    result = []
    return [] if not root else self.preorderRecursive(root, result)
