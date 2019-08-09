class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

finalResult = 807
print (finalResult)
def liste(finalResult):
    for digit in str(finalResult):
        head = tail = None
        node = ListNode(digit)
        print (node.val)
        if head is not None:
            tail.next = node
            tail = node
        else:
            head = node
            tail = node
    return head
node = liste(finalResult)
while (node is not None):
    print (node.val)
    node = node.next
