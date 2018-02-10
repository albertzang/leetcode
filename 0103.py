# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return list()
        cur = list([root])
        nxt = list()
        res = list()
        order = False
        while len(cur):
            res.append(map(lambda x: x.val, cur))
            for n in reversed(cur):
                if order:
                    if n.left is not None:
                        nxt.append(n.left)
                    if n.right is not None:
                        nxt.append(n.right)
                else:
                    if n.right is not None:
                        nxt.append(n.right)
                    if n.left is not None:
                        nxt.append(n.left)
            cur = nxt
            nxt = list()
            order = not order
        return res
