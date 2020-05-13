# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = []):
#         self.val = val
#         self.neighbors = neighbors
# """
from collections import deque
class Solution:
    def cloneGraph(self, node):
        if not node: return None
        root, clone = node, {}

        # BFS + Save node reference
        q , all_nodes = deque([node]) , set([node])
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in all_nodes:
                    q.append(neighbor)
                    all_nodes.add(neighbor)

        # Create Clone
        for node in all_nodes:
            clone[node] = Node(node.val)

        for node in all_nodes:
            for neighbor in node.neighbors:
                clone[node].neighbors.append(clone[neighbor])

        return clone[root]
