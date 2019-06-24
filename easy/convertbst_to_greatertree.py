# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    temp_total = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            # Traverse to last right child
            self.convertBST(root.right)
            self.temp_total += root.val  # Update the temp tally
            root.val = self.temp_total
            self.convertBST(root.left)  # Traverse left subtree
        return root