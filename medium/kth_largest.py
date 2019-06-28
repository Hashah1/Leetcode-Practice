import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Return k number of largest element
        # and select the last element from the returned list.
        return heapq.nlargest(k, nums)[k-1]