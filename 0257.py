# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            return list([str(root.val)])
        if root.left is None:
            return map(lambda x: '%s->%s' % (root.val, x), self.binaryTreePaths(root.right))
        if root.right is None:
            return map(lambda x: '%s->%s' % (root.val, x), self.binaryTreePaths(root.left))
        else:
            return map(lambda x: '%s->%s' % (root.val, x), self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right))
