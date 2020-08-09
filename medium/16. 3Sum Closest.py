from heapq import heappop, heappush, heapify

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Strategy:
        Find triplets with sum closest to target.
        1. Get list of all triplets generated from each pivoted element along with its sum
        2. Store (dev from target, sum) pair in heap (min_heap).
        3. Process heap to get largest element <= target
        TC: O(nlogn)
        SC: TC
        """
        nums.sort()
        heap = []
        for idx in range(len(nums) - 2):
            a = nums[idx]
            # Find the two other elements of triplet
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                sum_ = a + b + c
                dev = abs(target - sum_)
                # If triplet has target sum then best scenario
                if sum_ == target:
                    return target
                # Adjust parameters
                elif sum_ > target:
                    # Avoid duplicates
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                else:
                    # Avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                # Add to heap
                heappush(heap, (dev, sum_))
        # Return the top sum_ from the heap which is bound to have smallest deviation from the target
        return heappop(heap)[1]
