class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        SC = TC = O(d * f * t)
        """
        dp = [[0 for col in range(target + 1)] for row in range(d + 1)]
        mod_val = 10**9 + 7
        dp[0][0] = 1 # Only 1 way to roll 0 dices to get to target of 0
        # One dice can reach a target as long as its <= faces.
        for col in range(1, min(f + 1, target + 1)):
            dp[1][col] = 1

        # General case fill up
        for row in range(2, d + 1):
            for col in range(2, target + 1):
                # Recurrence relation:
                # dp[row][col] = dp[row - 1][col - 1] .. dp[row - 1][col - f]
                dependency_sum = 0
                starting = max(col - f, 0)
                for cur_face in range(starting, col):
                    dependency_sum += dp[row - 1][cur_face]
                dp[row][col] = dependency_sum % mod_val
        return dp[-1][-1]