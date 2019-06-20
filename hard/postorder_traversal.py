# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    traversal_list = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.traversal_list = []
        return self.iterative_sol(root)
        
    def recursive_sol(self,root):
        if root:
            left = self.recursive_sol(root.left)
            right = self.recursive_sol(root.right)
            self.traversal_list.append(root.val)
        return self.traversal_list

    def iterative_sol(self,root):
        stk = []
        if not root:
            return self.traversal_list
        while True:
            while root:
                # Push right child and then root
                if root.right:
                    stk.append(root.right)
                stk.append(root)
                # Set root to left child
                root = root.left
            root = stk.pop()
            # If new root's right child exists,
            if root.right and len(stk) > 0 and (root.right == stk[-1]):
                stk.pop()
                stk.append(root)
                root = root.right
            else:
                self.traversal_list.append(root.val)
                root = None
            if not stk:
                print("returning")
                return self.traversal_list