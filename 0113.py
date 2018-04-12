# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [[root.val]] if root.val == sum else []
        else:
            paths = []
            if root.left is not None:
                for path in self.pathSum(root.left, sum - root.val):
                    paths.append([root.val] + path)
            if root.right is not None:
                for path in self.pathSum(root.right, sum - root.val):
                    paths.append([root.val] + path)
            return paths
