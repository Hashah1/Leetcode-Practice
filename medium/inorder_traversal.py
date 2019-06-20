# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    traversal_list = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traversal_list = []
        return self.iterative_sol(root)
    def recursive_sol(self,root):    
        # Terminating condition.
        if root:
            self.recursive_sol(root.left)
            self.traversal_list.append(root.val)
            self.recursive_sol(root.right)
        return self.traversal_list

    
    def iterative_sol(self,root):
        stk = []
        if not root:
                return self.traversal_list
        while True:
            # Go left until node is null
            while root:
                stk.append(root)  # Keep adding to stack
                root = root.left
            if not root:
                if stk:
                    # Pop off stack and add to list
                    node = stk.pop()
                    self.traversal_list.append(node.val)
                    root = node.right
                else:
                     return self.traversal_list