class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        slowPointer = head
        fastPointer = head.next
        while (fastPointer != slowPointer):
            if not fastPointer or not fastPointer.next:
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return True
'''
We will have two pointers, one moving two steps each time and one moving one step.
The moment they meet, we know that there is a cycle.
Once the fast one reaches Null we know that the list has no cycle and return false


Time Complexity: O(n) as we visit each node once
Space Complexity: O(1) since we only allocate space for two pointers each time
'''
