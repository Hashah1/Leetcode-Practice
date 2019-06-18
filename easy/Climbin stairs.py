def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    # Use bottom up approach
    # Store the 0 and 1 step ways in list
    stored_results_list = [1,1]
    for each_way in range(1,n):
        # Store the num of ways to climb n'th step.
        # The num step is the current step + previous step
        stored_results_list.append(stored_results_list[each_way] + stored_results_list[each_way - 1])
    return stored_results_list.pop()

if __name__ == "__main__":
    # climbStairs(2)
    pass