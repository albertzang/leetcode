# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        parent = dummy
        runner = head
        i = 1
        while runner is not None and i <= n:
            tmp = runner.next
            if i < m:
                parent = runner
            elif i == m:
                end = runner
            else:
                runner.next = parent.next
                parent.next = runner
            runner = tmp
            i += 1
        end.next = runner
        return dummy.next
