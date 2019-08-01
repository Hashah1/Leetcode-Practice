# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.get_unival_subtree(root)
        return self.count

    def get_unival_subtree(self, root):
        if not root:
            return True
        left = self.get_unival_subtree(root.left)
        right = self.get_unival_subtree(root.right)
        if not left or not right:
            return False
        
        if (root.left and root.left.val != root.val):
            return False
        if (root.right and root.right.val != root.val):
            return False
        self.count += 1
        return True