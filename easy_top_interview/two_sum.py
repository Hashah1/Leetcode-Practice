class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            tmp = target - nums[i]
            nums[i] = None
            try:
                return [i, nums.index(tmp)]
            except:
                continue