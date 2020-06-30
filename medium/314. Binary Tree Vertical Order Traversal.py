# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Time Complexity: O(NLogN)
        Space Complexity: O(N)
        """
        self.all_nodes = []
        # Grab all nodes.
        self.dfs(root, 0, 0)

        # Sort for desired order based on the row and col
        self.all_nodes.sort(key = lambda x: x[0:2])

        # Aggregate based off col
        mapping = defaultdict(list)
        for col, row, val in self.all_nodes:
            mapping[col].append(val)
        return mapping.values()


    def dfs(self, root, row, col):
        if not root:
            return
        # Add vals (col, row, val) as priority should be left to right, top to bottom
        self.all_nodes.append((col, row, root.val))
        self.dfs(root.left, row + 1, col - 1)
        self.dfs(root.right, row + 1, col + 1)
