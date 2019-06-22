class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        # Find pivot
        pivot_index = nums.index(max(nums))
        # Check if the value is at the pivot index to avoid calling serach
        if target is nums[pivot_index]:
            return pivot_index
        # Search left of the pivot
        elif nums[0] <= target:
            return self.binarysearch(0, pivot_index - 1, nums, target)
        else:
            return self.binarysearch(pivot_index + 1, len(nums) - 1, nums, target)

    def binarysearch(self, l, r, list_1, target):
        if r >= l:
            middle_index = l + (r - l)/2
            print(middle_index)
            if list_1[middle_index] == target:
                return middle_index
            elif list_1[middle_index] > target:
                return self.binarysearch(l, middle_index - 1 , list_1, target)
            else:
                return self.binarysearch(middle_index + 1, r, list_1, target)
        else:
            return -1
        
   