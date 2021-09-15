l1 = [2,4,3]
l2 = [5,6,4]
# [7, 0, 8]

def addTwoNumbers(l1, l2):
    def reverseList(head):
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
	
        return prev

    print(reverseList(l1))
    print(reverseList(l2))
    return


addTwoNumbers(l1, l2)