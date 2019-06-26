# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # can perform a depth first search
        # can say that 2^i - 1 2 4 8 16 is when we increment depth
        if not root:
            return 0
        level = [root]
        depth = 0
        while level:
            queue = []
            depth += 1
            for node in level:
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
            level = queue
        return depth
        
