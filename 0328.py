# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            oh = head
            eh = head.next
            ot = oh
            et = eh
            while ot.next and et.next:
                ot.next = et.next
                ot = ot.next
                et.next = ot.next
                et = et.next
            ot.next = eh
        return head
