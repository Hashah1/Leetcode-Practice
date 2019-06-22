class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root:
            # No point in traversing left
            if root.val > R:
                return self.rangeSumBST(root.left,L,R)
            elif root.val < L:
                return self.rangeSumBST(root.right,L,R)
            else:
                # traversal: Left, Right
                return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        else:
            return 0