class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        TC = SC = O(all nodes in matrix)
        """
        # For caching.
        cache = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        LIP = 0
        # Up, Down Left Right
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_within_bounds(r, c):
            return (0 <= r < len(cache)) and (0 <= c < len(cache[0]))
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            for nei_r, nei_c in neighbors:
                x = i + nei_r
                y = j + nei_c
                # Check to see if the value is increasing and within bounds
                if is_within_bounds(x, y) and matrix[x][y] > matrix[i][j]:

                    cache[i][j] = max(cache[i][j], dfs(x, y))
            cache[i][j] += 1
            return cache[i][j]

        for r in range(len(cache)):
            for c in range(len(cache[0])):
                LIP = max(dfs(r, c), LIP)
        return LIP