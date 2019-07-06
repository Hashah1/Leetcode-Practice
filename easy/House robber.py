class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Previous max holds the most recent sum of robberies
        # Previous max holds the sum two houses before
        prev_max = prev_prev_max = tmp = 0
        for num in nums:
            prev_prev_max = tmp
            tmp = prev_max
            # Max is either the most recent sum, or the sum of robberies
            # two houses ago.
            prev_max = max(prev_max, prev_prev_max + num)
        return prev_max