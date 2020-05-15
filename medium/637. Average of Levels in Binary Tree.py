
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        Time Complexity: O(n), n = number of nodes in tree
        Space Complexity: O(2^depth), depth is depth of tree
        """
        q = deque([root])
        averages = []
        while q:
            level_len = len(q)
            sum_per_level = 0
            for _ in range(level_len):
                root = q.popleft()
                sum_per_level += root.val
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            average = sum_per_level / level_len
            averages.append(average)
        return averages

