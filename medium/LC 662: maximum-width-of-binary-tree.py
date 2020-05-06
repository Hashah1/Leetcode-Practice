# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Add position of starting node
        q = deque([(root, 0)])
        max_dist = 0
        while q:
            # Get width based on what's in the queue currently.
            # Update the max distance
            right_pos = q[-1][1]
            left_pos = q[0][1]
            max_dist = max(max_dist, right_pos - left_pos + 1)
            # For each level, update the child nodes
            for _ in range(len(q)):
                node, dist = q.popleft()
                # Add children with respective distances to queue.
                if node.left: q.append((node.left, 2*dist))
                if node.right: q.append((node.right, 2*dist + 1))
        return max_dist

