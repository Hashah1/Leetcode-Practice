class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # TC = SC = O(len(grid)*len(grid[0]))
        if not grid or not grid[0]:
            return 0
        # Create DP array
        # dp[i][j] == max num of kills when bomb placed here
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # Need to populate dp table by making following passes:
        # Row-wise: -> and <- traversal and mark enemies who die
        # column-wisee: up and down traversal and mark enemies who die
        self.mark_rows(grid, dp)
        self.mark_cols(grid, dp)

        # Get the max kills by one traversal
        return max(dp[i][j] for i in range(len(dp)) for j in range(len(dp[0])))

    def mark_cols(self, grid, dp):
        # Top to bottom
        for c in range(len(grid[0])):
            num_enemies = 0
            for r in range(len(grid)):
                # print(c, r)
                if grid[r][c] == "0":
                    dp[r][c] += num_enemies
                elif grid[r][c] == "E":
                    num_enemies += 1
                else:
                    num_enemies = 0

        # Bottom to top
        for c in range(len(grid[0])):
            num_enemies = 0
            for r in range(len(grid) - 1, -1, -1):
                if grid[r][c] == "0":
                    dp[r][c] += num_enemies
                elif grid[r][c] == "E":
                    num_enemies += 1
                else:
                    num_enemies = 0

    def mark_rows(self, grid, dp):
        # Left to right traversal
        for r in range(len(grid)):
            num_enemies = 0
            for c in range(len(grid[0])):
                if grid[r][c] == "0":
                    dp[r][c] += num_enemies
                elif grid[r][c] == "E":
                    num_enemies += 1
                else:
                    num_enemies = 0
        # Right to left traversal
        for r in range(len(grid)):
            num_enemies = 0
            for c in range(len(grid[0]) - 1, -1, -1):
                if grid[r][c] == "0":
                    dp[r][c] += num_enemies
                elif grid[r][c] == "E":
                    num_enemies += 1
                else:
                    num_enemies = 0