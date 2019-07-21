# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        isVisited = set()
        while head:
            if head in isVisited:
                return True
            isVisited.add(head)
            head = head.next
        return False


'''
For Brute Force we can just go through the entire list and see if it ends up looping back around
Could have a dictionary mapping the node with whether it was visited prior
Using this we could keep track of whether a given node occurs more than once letting us know of a cycle
'''
"""
:type head: ListNode
:rtype: bool
"""
