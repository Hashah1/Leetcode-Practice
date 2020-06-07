# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Brute force: Inorder traversal, return kth element O(2^height of tree)
        """
        inorder_trav = []
        def helper(node):
            if not node:
                return
            # Inorder
            helper(node.left)
            inorder_trav.append(node.val)
            helper(node.right)
        helper(root)
        return inorder_trav[k - 1]