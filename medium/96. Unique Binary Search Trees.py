class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time Complexity: O(n2)
        Space Complexity: O(n)
        """
        # Create DP list of range(n + 1)
        dp = [0] * (n + 1)
        # Number of Uniquie BSTs from 0 and 1 nodes are 1
        dp[0], dp[1] = 1, 1

        for num in range(2, n + 1):
            for node in range(num + 1):
                dp[num] += dp[node - 1] * dp[num - node]
        return dp[-1]