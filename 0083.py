# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        n = head
        while n.next is not None:
            if n.val == n.next.val:
                n.next = n.next.next
            else:
                n = n.next
        return head
