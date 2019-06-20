# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    traversal_list = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traversal_list = []
        return self.iterative(root)
    
    def recursive(self,root):
        if root:
            self.traversal_list.append(root.val)
            left = self.recursive(root.left)
            right = self.recursive(root.right)
        return self.traversal_list
    
    def iterative(self,root):
        stk = []
        if root:
            # Add root to stack
            stk.append(root)
            while stk:
                node = stk.pop()
                self.traversal_list.append(node.val)
                # Push right and left children to stack
                if node.right:
                    stk.append(node.right)
                if node.left:
                    stk.append(node.left)
            return self.traversal_list
        return self.traversal_list
            
        