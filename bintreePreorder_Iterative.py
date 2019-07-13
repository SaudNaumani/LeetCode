def preorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    result = []
    curr = root
    stack.append(curr)
    while (stack):
        # pop and print
        curr = stack.pop()
        if curr is not None:
            # push right child first, then push left child
            result.append(curr.val)
            if (curr.right):
                stack.append(curr.right)
            if (curr.left):
                stack.append(curr.left)
    return result
