# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path = []

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Populate path to find p
        self.has_path(root, p)
        path_p = self.path
        self.path = []
        # Populate path to find q
        self.has_path(root, q)
        path_q = self.path

        LCA = None
        # Return the last node where p and q's lists were equal.
        while path_p and path_q:
            p = path_p.pop(0)
            q = path_q.pop(0)
            if p == q:
                LCA = p
            else:
                break
        return LCA

    def has_path(self, root, target):
        """
        Find path to target node and populates a list with it.
        """
        # If we find target, return
        if not root:
            return False
        # Store the path to a list
        self.path.append(root)
        if root == target or self.has_path(root.left, target) or self.has_path(root.right, target):
            return True
        self.path.pop()
        return False