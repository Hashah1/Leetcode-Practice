# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            """
            Helper to build the tree.
            """
            # Left bound should always be less than right bound
            if left > right:
                return
            # Get the root from preorder list
            val = preorder.pop(0)
            # Create node from value
            node = TreeNode(val)
            # Get the index of the same root from inorder list
            index = mapping[val]
            # Recurse through right side with elements in inorder tree > index
            node.right = helper(index + 1, right)
            # Do the same for left side
            node.left = helper(left, index - 1)
            return node
        mapping = {}
        for i, val in enumerate(inorder):
            mapping.update({val:i})
        return helper(0, len(preorder) - 1)

if __name__ == "__main__":
    a = Solution()
    a.buildTree(
        [3,9,20,15,7],
        [9,3,15,20,7]
    )
    pass