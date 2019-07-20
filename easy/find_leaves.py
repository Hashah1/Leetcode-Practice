# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.res = []

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        leaves = []
        if root:
            while not self.is_leaf(root):
                self.helper(root)
                leaves.append(self.res)
                self.res = []
            leaves.append([root.val])
        return leaves

    def helper(self, root):
        """
        DFS
        """
        if not root:
            return
        if self.is_leaf(root.left):
            self.res.append(root.left.val)
            root.left = None
        if self.is_leaf(root.right):
            self.res.append(root.right.val)
            root.right = None
        self.helper(root.left)
        self.helper(root.right)

    def is_leaf(self, node):
        if node:
            if not (node.left or node.right):
                return True
        return False