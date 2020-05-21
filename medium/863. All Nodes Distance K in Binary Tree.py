# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        Strategy:
        1. Mark all node's parents
        2. At this point, each node will have its left, right and parent neighbors -> Ultimately tree has been converted to a graph.
        3. BFS on the "graph" and once distance of K is reached,return result.

        Time Complexity: O(2^h), h = height of tree (log(num nodes)).
        Space Complexity: O(2^h), h = height of tree. Same as O(num_nodes)
        """
        child_parent_map = {}
        def dfs(node, parent = None):
            if node:
                child_parent_map[node] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        # Start off from target node and bfs from there.
        # Each element of queue will contain (node, distance)
        q = deque([(target, 0)])
        seen = set([target])
        while q:
            cur_node, cur_dist = q.popleft()
            if cur_dist == K:
                # Return cur node and all nodes in q. At this point all nodes in q
                # have all nodes K distance away, and no point going further.
                return [cur_node.val] + [prev_node.val for prev_node, _ in q]
            seen.add(cur_node)

            # Iterate over left, right, parent nodes.
            for neighbor in (cur_node.left, cur_node.right, child_parent_map[cur_node]):
                if neighbor and neighbor not in seen:
                    q.append((neighbor, cur_dist + 1))
        return []
