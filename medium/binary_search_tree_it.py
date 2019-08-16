# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.bst = []
        self.convert_to_list(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.bst.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.bst else False

    def convert_to_list(self, root):
        """
        Convert the BST to a list via inorder traversal
        """
        if not root:
            return
        self.convert_to_list(root.left)
        self.bst.append(root.val)
        self.convert_to_list(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()