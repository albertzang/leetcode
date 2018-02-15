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
        if head is None or head.next is None:
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            if head.val == head.next.val:
                while head.next is not None and head.val == head.next.val:
                    head = head.next
                dummy.next = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
            return dummy.next
