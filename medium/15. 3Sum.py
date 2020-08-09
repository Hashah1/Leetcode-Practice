class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Thought process:
        For each current eelement in nums, place a on current element.
        then search entire array for suitable b and c elements.
        O(len(nums) ^ 2)
        """
        def get_pair(target, idx):
            # Find b and c such that b + c = -a
            pairs = []
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ == target:
                    pairs.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 # Duplicates handle
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 # Duplicates handle
                    left += 1
                    right -= 1
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1
            return pairs

        res = []
        nums.sort()
        for idx in range(len(nums) - 2):
            num = nums[idx]
            if idx > 0 and num == nums[idx - 1]:  # Preevent duplicatees
                continue
            pairs = get_pair(-1*num, idx)
            for p in pairs:
                res.append([num] + p)

        return res