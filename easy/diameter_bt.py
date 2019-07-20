# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diam = 0
        def get_max_depth(root):
            if not root:
                return 0
            left = get_max_depth(root.left)
            right = get_max_depth(root.right)
            self.max_diam = max(left + right, self.max_diam)
            return max(left,right) + 1

        get_max_depth(root)
        return self.max_diam


