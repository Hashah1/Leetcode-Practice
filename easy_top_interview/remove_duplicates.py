class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        while index < len(nums) - 1:
            # For each element, check if the next element is the same
            # If it is, delete, otherwise go next step
            if nums[index] == nums[index + 1]:
                del nums[index]
            else:
                index += 1
        return len(nums)