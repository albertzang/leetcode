# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        runner = head
        length = 0
        while runner is not None:
            length += 1
            runner = runner.next
        (node, flag) = self._isPalindrome(head, length)
        return flag

    def _isPalindrome(self, head, length):
        if length == 0:
            return (head, True)
        elif length == 1:
            return (head.next, True)
        (node, flag) = self._isPalindrome(head.next, length - 2)
        if flag:
            return (node.next, node.val == head.val)
        else:
            return (node.next, flag)
