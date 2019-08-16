# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # Get target node.
        target_node = self.searchBST(root, key)
        parent = None
        successor = target_node

        # If two children, find next successor and swap
        if target_node.left and target_node.right:
            if self.is_leaf(successor.right):
                target_node.val = successor.right.val
                successor.right = None
                return root
            else:
                successor = successor.right
                while successor.left:
                    print("at {}".format(successor))

                    # Break at the parent of successor
                    if self.is_leaf(successor.left):
                        print("Breaking at {}".format(successor))
                        break
                    successor = successor.left
                target_node.val = successor.left.val
                successor.left = None # Cut reference to the successor.
        elif target_node.right or target_node.left:
            if target_node.right:
                target_node.val = target_node.right.val
                target_node.right = None
            elif target_node.left:
                target_node.val = target_node.left.val
                target_node.left = None
        else:
            target_node = None
        return root

    def is_leaf(self, root):
        return True if not (root.left or root.right) else False
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val == val:
            return root
        if val <= root.val:
            return self.searchBST(root.left,val)
        elif val > root.val:
            return self.searchBST(root.right,val)