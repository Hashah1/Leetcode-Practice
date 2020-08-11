class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]

        # Change first row and col to become cumulative sum of grid's row and col resp.
        # Row
        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        # Col
        for i in range(1, len(grid[0])):
            dp[0][i] = grid[0][i] + dp[0][i - 1]

        # Go over dp and the dp[i][j] = grid[i][j] + min(top of dp, left of dp)
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                dp[r][c] = grid[r][c] + min(dp[r][c - 1], dp[r - 1][c])
        return dp[-1][-1]