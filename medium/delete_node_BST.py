# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root:
            # Find the target node to delete
            if key == root.val:
                # Delete
                # Case 1: If it is leaf node:
                if not root.right and not root.left:
                    root = None
                elif root.right:
                    # Find successor and attach it to current node
                    tmp = self.get_successor(root)
                    root.val = tmp.val
                    # Delete the successor node down the tree
                    root.right = self.deleteNode(root.right, tmp.val)
                else:
                    tmp = self.get_predeccessor(root)
                    root.val = tmp.val
                    # Delete the successor node down the tree
                    root.left = self.deleteNode(root.left, tmp.val)
            elif key > root.val:
                # Traverse right
                root.right = self.deleteNode(root.right, key)
            else:
                # Traverse left
                root.left = self.deleteNode(root.left, key)
        return root
    
    def get_successor(self, root):
        """
        Useful when successor is to the right of root.
        """
        # Take a right traversal and go left
        # As much as you can. Last node will be successor
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def get_predeccessor(self, root):
        """
        Useful when successor is the parent of root.
        Get predeccessor instead.
        """
        # Take a right traversal and go left
        # As much as you can. Last node will be successor
        root = root.left
        while root.right:
            root = root.right
        return root