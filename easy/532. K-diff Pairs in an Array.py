class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Strategy:
        Brute:
        O(len(nums)^2) -> get all unique pairs of diff k.

        Optimized: TC = O(len(nums)), SC = O(len(nums))
        Sort the nums
        Two pointers,
        if diff > k, move left ptr
        if diff < k, move right ptr
        if diff == k: add
        if ptrs are same, move right
        """
        nums.sort()
        seen = set()
        i = 0
        j = 1
        count = 0
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
                continue
            diff = abs(nums[i] - nums[j])
            if diff == k and (nums[i], nums[j]) not in seen:
                count += 1
                seen.add((nums[i], nums[j]))
                i += 1
                j += 1
            elif diff > k:
                i += 1
            else:
                j += 1
        return count