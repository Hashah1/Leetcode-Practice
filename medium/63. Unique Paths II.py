class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # SC = TC = O(all nodes in obstacle grid)
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for col in range(len(obstacleGrid[0]) + 1)] for row in range(len(obstacleGrid) + 1)]
        dp[1][1] = 1 # 1 path to reach top left corner
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if row == 1 and col == 1:
                    continue
                if obstacleGrid[row - 1][col - 1] == 1:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]