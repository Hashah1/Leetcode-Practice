def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Sort
    nums = sorted(nums)
    n = len(nums) - 1

    # Max will either be last 3
    # Or first two and last 1 (if negative)
    max1 = max(
        nums[0]*nums[1]*nums[n],
        nums[n]*nums[n-1]*nums[n-2]
    )
    return max1
        

if __name__ == "__main__":
    maximumProduct([-4,-3,-2,-1,60])
    maximumProduct([-1,-1,1])
    maximumProduct([-1,-2,1,2,3])
    pass