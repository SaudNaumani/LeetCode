def postorderTraversal(self, root: TreeNode) -> List[int]:
   return [] if not root else self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
