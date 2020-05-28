class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Time Complexity:
        1. Graph Creation
            O(len(equations))

        2. DFS for each query
            UPDATED: O(len(queries) * len(equations))
        Space Complexity:
        O(len(equations))

        """
        graph = defaultdict(list)
        seen = set()
        answers = []
        # Create graph
        for idx, pair in enumerate(equations):
            graph[pair[0]].append((pair[1], values[idx]))
            graph[pair[1]].append((pair[0], 1/values[idx]))
        # Get calculation for each query.
        for query in queries:
            cur_node, target_node = query
            if cur_node not in graph:
                answers.append(-1.0)
            else:
                answers.append(self.dfs_helper(cur_node, target_node, graph, seen))
            seen.clear()
        return answers

    def dfs_helper(self, cur_node, target_node, graph, seen, result=1.0):
        seen.add(cur_node)
        if cur_node == target_node:
            return result
        for neighbor, cost in graph[cur_node]:
            if neighbor not in seen:
                ans = self.dfs_helper(neighbor, target_node, graph, seen, result*cost)
                if ans != -1.0:
                    return ans
        return -1.0
