def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Set initial sums to the first element
        previous_max = current_max = nums[0]
        # Iterate through everything after first number
        # Compare the current num and the 
        # previous sum of numbers leading to it.
        # Maximum sum is the max of the two
        for i in range(1, len(nums)):
            # Get the max and set it to the previous_max
            previous_max = max(nums[i], nums[i] + previous_max)
            if previous_max > current_max:
                current_max = previous_max
        return current_max

