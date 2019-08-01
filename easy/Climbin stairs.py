class Solution(object):
    def climbStairs(self, n):
        """ RECURSIVE
        :type n: int
        :rtype: int
        """
        # Cache with stairs:numways relationship
        cache = {}
        def helper(n):
            # Base case 1
            if n in cache:
                return cache[n]
            # Base case 2
            if n < 2:
                return 1

            res = helper(n - 1) + helper(n - 2)
            cache[n] = res
            return res
        return helper(n)

    # def climbStairs(self, n):
    #     """ ITERATIVE
    #     :type n: int
    #     :rtype: int
    #     """
    #     # Use bottom up approach
    #     # Store the 0 and 1 step ways in list
    #     stored_results_list = [1,1]
    #     for each_way in range(1,n):
    #         # Store the num of ways to climb n'th step.
    #         # The num step is the current step + previous step
    #         stored_results_list.append(stored_results_list[each_way] + stored_results_list[each_way - 1])
    #     return stored_results_list.pop()