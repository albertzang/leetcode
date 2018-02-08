# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        d = dummy
        p = d.next
        while p is not None and p.next is not None:
            q = p.next
            p.next = q.next
            q.next = p
            d.next = q
            d = p
            p = p.next
        return dummy.next
