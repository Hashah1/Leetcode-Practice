# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.has_sum(root,sum,0)

    def has_sum(self, root, sum, max_sum):
        if not root:
            return False
        max_sum += root.val
        if not (root.left or root.right) and sum == max_sum:
            return True
        return self.has_sum(root.left, sum, max_sum) or self.has_sum(root.right, sum, max_sum)