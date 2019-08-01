from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def levelOrder(root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            res = []  # Holds list of all levels

            if root:
                queue = deque([root,])  # Add root to the queue
                while queue:
                    level = []
                    level_len = len(queue)
                    for i in range(level_len):
                        node = queue.popleft()
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                        level.append(node)
                    res.append(level)
            return res
        # Get list of all nodes on the same level
        levels = levelOrder(root)
        # For each item inside a list, populate the 'next' node to point to the next node.
        for level in levels:
            for i in range(len(level)):
                try:
                    if level[i + 1]:
                        level[i].next = level[i + 1]
                except:
                    pass
        return root