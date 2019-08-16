# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # Get the inorder traversal of tree. If not sorted in ascending order, its not a BST
        inorder_trav = self.inorder(root,[])
        # Return true if list returned from inorder traversal is sorted, else return false
        return True if(all(inorder_trav[i] < inorder_trav[i + 1] for i in range(len(inorder_trav)-1))) else False

    def inorder(self, node, inorder_trav):
        """Inorder traversal of BST"""
        if not node:
            return
        self.inorder(node.left, inorder_trav)
        inorder_trav.append(node.val)
        self.inorder(node.right, inorder_trav)
        return inorder_trav