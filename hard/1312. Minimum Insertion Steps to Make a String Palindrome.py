class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Strategy: SC = O(len(s)^2), TC = O(len(s)^2/2)
        Build up to the top right from main diagonal.

        Let DP(i, j) be the min number of steps needed to make s[i:j] a palindrome.

        1. Build main diagonal, where all substrings of length 1 are 0 since already a palindrome
        2. Build next diagonal to the right of it for all strings of length 2
        3. General case:
            If s[i] == s[j], then grab the bottom left of current cell
            else: Grab max from left and bottom and add 1
        """
        dp = [[0 for col in range(len(s))] for row in range(len(s))]
        # 1. Already done.
        # 2.
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                dp[i][i + 1] = 1
        # 3. Iterate from 3rd last bottom row and move up
        for row in range(len(s) - 3, -1, -1):
            for col in range(row + 2, len(s), 1):
                if s[row] == s[col]:
                    dp[row][col] = dp[row + 1][col - 1]
                else:
                    dp[row][col] = min(dp[row][col - 1], dp[row + 1][col]) + 1
        # Ans should be in top right
        return dp[0][-1]