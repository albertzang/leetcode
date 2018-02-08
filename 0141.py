# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        q = head
        while p is not None and q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False
