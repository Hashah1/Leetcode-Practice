# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        """
        Time Complexity: O(n), n = total nodes
        Space COmplexity: O(2^d), d = depth of tree
        """
        if not root:
            return []
        q = deque([root])
        largests = []

        while q:
            level_len = len(q)
            max_per_level = float('-inf')
            for _ in range(level_len):
                root = q.popleft()
                max_per_level = max(max_per_level, root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            largests.append(max_per_level)
        return largests
