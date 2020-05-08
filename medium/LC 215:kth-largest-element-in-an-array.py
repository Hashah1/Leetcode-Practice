from heapq import heapify, heappop
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Brute Force: Time Complexity: O(nlog(n)) n = len(nums). Space COmplexity: O(1)
        # Sort nums.
        # Return the kth valued element in sorted order (from tail of the list). Make sure k'th iterator changes based
        # off different element value -> O(k)

        def min_heap():
            """
            Time Complexity: O(nlogn + c), c = len(nums) - K
            Space Complexity: O(n)
            Strategy.
            Heapify nums -> O(nlogn), n = len(nums)
            Pop from heap from i...len(nums) - K times, idx changes based off every different element seen
            Return first element from the heap
            """
            heap = nums[:] # O(n)
            heapify(heap) # Log(n)
            i = 0
            prev = None
            while i < len(nums) - k:
                cur = heappop(heap)
                if cur != prev:
                    i += 1
            return heap[0]

        def max_heap():
            """
            Time Complexity: O(nlogn + k)
            Space Complexity: O(n)

            Strategy:
            Max_heapify the nums array: O(nlogn)
            Pop kth element from heap: O(k)
            """
            heap = [-num for num in nums]
            heapify(heap)
            i = 0
            prev = None
            while i < k - 1:
                cur = heappop(heap)
                if cur != prev:
                    i += 1
            return heap[0]
