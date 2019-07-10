class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        # Calculate the number of ways n'th fence
        # can be painted in k colors.
        # 1. n = 1, can be painted k ways. 
        total_diff_ways = k * (k-1)
        same = k

        # 2. n = 2, can be painted 2 times the same way, or k(k-1) times differently.
        # The total num ways is num_ways to color same and different (total = same + different)
        for i in range(3, n + 1):
            same = total_diff_ways
            total_diff_ways = (same + total_diff_ways) * (k - 1)
        return same + total_diff_ways
if __name__ == "__main__":
    a = Solution()
    a.numWays(2,3)