class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = [[0 for i in range(len(grid))] for j in range(len(grid[0]))]
        def dfs(row, col, cur_size):
            if grid[row][col] == 0:
                return 0
            if memo[row][col]:
                return memo[row][col]
            cur_size += 1
            visited.add((row, col))

            for neighbor in adj:
                nei_r = row + neighbor[0]
                nei_c = col + neighbor[1]
                if (nei_r, nei_c) not in visited and is_within_bounds(nei_r, nei_c):
                    ret = dfs(nei_r, nei_c, cur_size)
                    cur_size = max(ret, cur_size)
                    memo[row][col] = cur_size
            return memo[row][col]

        def is_within_bounds(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        # DRIVER
        max_size = 0
        has_explored = False
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0: # Try flip and dfs
                    grid[row][col] = 1
                    ret_size = dfs(row, col, 0)
                    max_size = max(max_size, ret_size)
                    visited.clear()
                    grid[row][col] = 0  # Backtrack

                    has_explored = True
        return max_size if has_explored else len(grid[0]) * len(grid)
