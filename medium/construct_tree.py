# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(left_index, right_index):
            # If tree can't be split
            if left_index > right_index:
                # Nothing to split
                return None
            # Remove last node as root
            postorder_root = postorder.pop()
            node = TreeNode(postorder_root)

            # Get index of root in inorder list
            index = mapping[postorder_root]

            # Right subtree is everything after root's index
            node.right = helper(index + 1, right_index)
            # Left subtree is everything before root's index
            node.left = helper(left_index, index - 1)
            return node
        # Build mapping of inorder traversal value and its index
        mapping = {}
        for index, val in enumerate(inorder):
            mapping.update({val: index})
        return helper(0, len(inorder) - 1)

