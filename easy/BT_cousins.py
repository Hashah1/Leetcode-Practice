# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # Get depth of the two nodes.
        x_depth = self.get_depth(root, x, 0)
        y_depth = self.get_depth(root, y, 0)
        # Find parents
        parent_x = self.get_parent(root, x)
        parent_y = self.get_parent(root, y)
        if parent_x.val != parent_y.val:
            if x_depth == y_depth:
                return True
        return False

    def get_depth(self, root, target_val, depth):
        """
        Finds the depth of a target root from the tree's root node
        :param target_val: {Int} The target who's node equivalent's depth needs to be found
        :param root: {TreeNode} Root node passed in.
        :return depth: {Int} The depth of the node.
        """
        if not root:
            return 0
        if root.val == target_val:
            return depth
        left = self.get_depth(root.left, target_val, depth + 1)
        right = self.get_depth(root.right, target_val, depth + 1)
        return max(left, right)

    def get_parent(self, root, target_val):
        """
        Finds the parent of target node
        """
        if not root:
            return None
        if root.val == target_val:
            return root
        if root.right:
            if root.right.val == target_val:
                return root
        if root.left:
            if root.left.val == target_val:
                return root
        node = self.get_parent(root.left,target_val)
        if node:
            return node
        else:
            node = self.get_parent(root.right,target_val)
            if node:
                return node