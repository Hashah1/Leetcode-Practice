from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []  # Holds list of all levels
        curr_level = []  # Holds current level
        if not root: 
            return res
        q = deque([root, ]) # Append root to the queue
        while q:  # While queue is not empty
            level_len = len(q)  # Set bounds for new level
            for item in range(level_len):
                root = q.popleft()
                curr_level.append(root.val)
                # Populate the queue with the children of root.
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(curr_level)  # Once level is filled, add to result
            curr_level = []  # Clear the current level, as new level will start
        return res