# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self, node, target):
        res, diff = node.val, abs(target - node.val)
        if target > node.val and node.right:
            rres, rdiff = self.find(node.right, target)
            if rdiff < diff:
                return rres, rdiff
        if target < node.val and node.left:
            lres, ldiff = self.find(node.left, target)
            if ldiff < diff:
                return lres, ldiff
        return res, diff

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res, diff = self.find(root, target)
        return res
