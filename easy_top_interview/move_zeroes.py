class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums:
            break_val = len(nums) - 1
            index = 0
            while index <= break_val:
                if nums[index] is 0:
                    del nums[index]
                    nums.append(0)
                    break_val -= 1
                else:
                    index += 1
        pass
a = Solution()
a.moveZeroes([0, 2])