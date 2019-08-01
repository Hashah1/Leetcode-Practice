# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        r_a = r_b = root
        return self.traverse(r_a, r_b)

    def traverse(self,ra, rb):
        # If either of them are Null
        if not ra or not rb:
            # Check if both are null, return True
            # as the two nodes have traversed at same rate
            if not ra and not rb:
                return True
            return False
        # Traverse symmetrically
        left_mirror = self.traverse(ra.left, rb.right)
        right_mirror = self.traverse(ra.right, rb.left)
        # As long as each mirror node is same and the left and right subtrees are same
        # return True
        if ra.val == rb.val and left_mirror and right_mirror:
            return True