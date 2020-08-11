from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Create Graph, indegree graph
        BFS on the graph, with q built from all nodes with indegree = 0
        """
        graph, indeg = self.get_graph_and_indegree(numCourses, prerequisites)

        return self.bfs(graph, indeg, numCourses)

    def get_graph_and_indegree(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indeg = {}
        # Mark indegree starting points. Every node has indegree of 0
        for i in range(numCourses):
            indeg[i] = 0
        # Create the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] += 1
        return graph, indeg

    def bfs(self, graph, indeg, numCourses):
        q = deque([])
        # Build queue
        for node, indegree in indeg.items():
            if indegree == 0:
                q.append(node)

        res = []
        while q:
            node = q.popleft()
            res.append(node)
            if len(res) == numCourses:
                break

            # Go over neighbors
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []