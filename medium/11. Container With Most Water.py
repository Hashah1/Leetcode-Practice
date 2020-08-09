class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Thought process
        Goal: Find container with most water.
        Trick is to have best width vs height combo between two bounds.

        Start with sliding window approach.
        Reecord current max rectangle.
        Shorten window by moving smaller bar's index
        repeat
        return max -> O(len(height))
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            left_bar = height[left]
            right_bar = height[right]

            # Get area by min(bar1,bar2)*width
            area = min(left_bar, right_bar) * (right - left)
            max_area = max(area, max_area)
            if left_bar < right_bar:
                left += 1
            else:
                right -= 1
        return max_area