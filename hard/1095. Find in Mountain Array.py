# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        So in total: O(log(n)) -> n = len(mountain_arr)
        1 pass: Find peak
        2 pass: Find target left of peak
        3 pass: Find target right of peak
        """
        # Find peak
        peak_idx = self.get_peak_idx(mountain_arr)
        # Find target to left of peak
        left_targ = self.left_search(0, peak_idx, mountain_arr, target)
        if left_targ != -1:
            return left_targ
        # Find target to right of peak
        right_targ = self.right_search(peak_idx + 1, mountain_arr.length() - 1, mountain_arr, target)
        return right_targ

    def left_search(self, left, right, mountain_arr, target):
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            # Ptr iteration technique
            # Check if mid's value is a target
            if mid_val == target:
                right = mid
            # Move right if:
            elif mid_val > target:
                right = mid
            # Move left if:
            else:
                left = mid
        if mountain_arr.get(left) == target:
            return left
        if mountain_arr.get(right) == target:
            return right
        return -1

    def right_search(self, left, right, mountain_arr, target):
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            # Ptr iteration technique
            # Check if mid's value is a target
            if mid_val == target:
                left = mid
            # Move right if:
            elif mid_val > target:
                left = mid
            # Move left if:
            else:
                right = mid
        if mountain_arr.get(right) == target:
            return right
        if mountain_arr.get(left) == target:
            return left
        return -1

    def get_peak_idx(self, mountain_arr):
        left = 0
        right = mountain_arr.length() - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            right_val = mountain_arr.get(mid + 1)
            # Move right if:
            #   mid's next node is increasing
            if right_val >= mid_val:
                left = mid
            # Move left if:
            #   mid's next node is decreasing
            else:
                right = mid
        if mountain_arr.get(left) > mountain_arr.get(right):
            return left
        return right