# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.leftLeaves(root.left, True) + self.leftLeaves(root.right, False)

    def leftLeaves(self, node, left):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.val if left else 0
        elif node.left is None:
            return self.leftLeaves(node.right, False)
        elif node.right is None:
            return self.leftLeaves(node.left, True)
        else:
            return self.leftLeaves(node.left, True) + self.leftLeaves(node.right, False)
