class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # To memoize
        cache = {}

        def helper(N):
            # If the number we're trying to find is in cache,
            # return that
            if N in cache:
                return cache[N]
            # Base Case: If N=0 or N=1, return N
            if N < 2:
                return N
            # Otherwise, recurrence relation:
            result = helper(N-1) + helper(N-2)
            # Store result in cache for future purposes
            cache[N] = result
            return result
        return helper(N)