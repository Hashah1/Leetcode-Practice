class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Previous max holds the most recent sum of robberies
        prev_max = 0
        # Previous max holds the sum two houses before
        prev_prev_max = 0
        tmp = prev_max
        for num in nums:
            prev_prev_max = tmp
            tmp = prev_max
            # Max is either the most recent sum, or the sum of robberies
            # two houses ago.
            prev_max = max(prev_max, prev_prev_max + num)
        return prev_max
       
if __name__ == "__main__":
    a = Solution()
    a.rob([1,2,3,1])
    a.rob([2,7,9,3,1])