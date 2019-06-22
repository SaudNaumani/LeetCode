class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next
            carry, result = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(result)
            n = n.next
        return root.next
        
