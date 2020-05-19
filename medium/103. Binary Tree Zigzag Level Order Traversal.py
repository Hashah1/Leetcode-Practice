# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity: O(n) or 2^(log(n)), n = number of nodes in tree
        Space Complexity: O(n) or 2^(log(n)), n = number of nodes in tree
        """
        if not root:
            return []
        q = deque([root])
        all_levels = []
        go_right = True
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                if go_right: # Add from left to right
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                elif not go_right: # Go right to left
                    node = q.pop()
                    if node.right:
                        q.insert(0, node.right)
                    if node.left:
                        q.insert(0, node.left)
                level.append(node.val)
            all_levels.append(level)
            go_right = not go_right
        return all_levels
