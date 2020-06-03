class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # TC = O(len(nums)), SC = O(1)
        # Go over every element, negate num - 1's index.
        # Why -1? Because all elements are <= len(arr)
        # If duplicate is found, it will be negated again at some point in list.
        for num in nums:
            nums[abs(num) - 1] *= -1
        res = []
        for num in nums:
            # Any double negated value is a duplicate
            is_positive = nums[abs(num) - 1]
            if is_positive > 0:
                res.append(abs(num))
                # To prevent it being found again
                nums[abs(num) - 1] *= -1
        return res