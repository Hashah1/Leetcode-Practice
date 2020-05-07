from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points, K):
        """https://leetcode.com/problems/k-closest-points-to-origin/"""
        def min_heap_implementation():
            # Min Heap Implementation
            # Time Complexity: 2nlog(h) -> nlog(h), n = len(points), h = len(heap)
            # Space Complexity: O(K), K is the number of points closest to (0,0)
            # Strategy:
            # 1: Create a result min_heap which contains all distances
            # 2: Loop over all points, calculate its distance and add to heap along with its point
            # 3: Pop kth element from heap and add each popped element to result list

            heap = []
            for point in points: # O(n)
                e_dist = self.get_distance(point[0], point[1]) # O(1)
                heappush(heap, (e_dist, point)) # O(logh)
            res = []
            for i in range(K): # O(n)
                res.append(heappop(heap)[1]) # O(logh)
            return res

        def max_heap_implementation():
            """
            # Time Complexity: O(nlog(h) + O(c1log(h)) + O(K)
              where n = len(points), h = len(heap), c1 = len(heap) - K
            # Space Complexity: O(K)
            Strategy:
            # 1: Create a result max_heap which contains all (distance, point). To make max heap, -1*distance
            # 2: Loop over all points, calculate its distance and add to heap along with its point
            # 3: Pop kth element from heap and add each popped element to result list
            """
            heap = []
            for point in points: # O(n)
                e_dist = -1*self.get_distance(point[0], point[1]) # O(1)
                heappush(heap, (e_dist, point))  # O(logh)
            res = []
            for i in range(len(heap) - K):  # O(len(heap) - K) = O(c1)
                heappop(heap)  # O(logh)

            for i in heap:  # O(K)
                res.append(i[1])  # O(1)
            return res

    def get_distance(self, p_0, p_1):
        return (p_0**2 + p_1**2) ** 0.5


a = Solution()
a.kClosest([[1,3],[-2,2]], 1)