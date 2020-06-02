class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # TC: O(2*len(nums))
        nums.sort()
        # Ensure that 0 is at the first index
        if nums[0] != 0:
            return 0
        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)

        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                return nums[i] + 1