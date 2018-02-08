# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        runner = dummy
        while runner.next is not None:
            tmp = runner.next
            if tmp.val == val:
                runner.next = tmp.next
            else:
                runner = runner.next
        return dummy.next
