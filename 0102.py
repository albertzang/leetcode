# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return list()
        cur = list([root])
        nxt = list()
        res = list()
        while len(cur):
            res.append(map(lambda x: x.val, cur))
            for n in cur:
                if n.left is not None:
                    nxt.append(n.left)
                if n.right is not None:
                    nxt.append(n.right)
            cur = nxt
            nxt = list()
        return res
