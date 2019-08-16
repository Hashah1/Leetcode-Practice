# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if not root:
            return TreeNode(val)
        if val <= root.val:
            if not root.left:
                root.left = TreeNode(val)
                return root
            self.insertIntoBST(root.left, val)
        elif val > root.val:
            if not root.right:
                root.right = TreeNode(val)
                return root
            self.insertIntoBST(root.right, val)
        return root