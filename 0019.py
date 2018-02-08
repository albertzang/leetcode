# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        a = dummy
        b = dummy
        for _ in xrange(n):
            b = b.next
        while b.next is not None:
            a = a.next
            b = b.next
        a.next = a.next.next
        return dummy.next
