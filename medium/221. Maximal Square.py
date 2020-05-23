class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Time Complexity: O(row*col), row = len(matrix), col = len(matrix[0])
        Space Complexity: O(row * col), row = len(matrix), col = len(matrix[0])
        """
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        max_size = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1": # Validate matrix square
                    left = dp[row][col - 1]
                    up = dp[row - 1][col]
                    adj = dp[row - 1][col - 1]
                    dp[row][col] = min(left, up, adj) + 1
                    max_size = max(dp[row][col], max_size)
        return max_size ** 2