class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if (not l1) or (l2 and l1.val > l2.val):
			l1, l2 = l2, l1 ## 변수 스왑
		if l1:
			l1.next = self.mergeTwoLists(l1.next, l2)
		print(type(l1))
		return l1


def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return res.next


l1 = makeNode([1,2,4])
l2 = makeNode([1, 3, 4])
ans = Solution().mergeTwoLists(l1, l2)
# print(list(ans))
while ans:
    print(ans.val, end=' ')
    ans = ans.next


