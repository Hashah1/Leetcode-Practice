"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    res = []
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        return self.iterative(root)
    
    def recursive(self,root):
        if root:
            self.res.append(root.val)
            for i in root.children:
                self.recursive(i)
        return self.res
    
    def iterative(self,root):
        if not root:
            return []

        stack, output = [], []            
        stack.append(root)
        while stack:
            root = stack.pop()
            self.res.append(root.val)
            stack.extend(root.children[::-1])
        return self.res
