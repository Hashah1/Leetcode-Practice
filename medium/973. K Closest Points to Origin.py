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
            
            # UPDATE: TC =  nlog(n) + Klog(n)
            #         SC = O(n) + O(K)
            heap = []
            for point in points: # O(n), n = len(points)
                e_dist = self.get_distance(point[0], point[1]) # O(1)
                heappush(heap, (e_dist, point)) # O(logh) x O(log(n)), n = total nodes in tree., log(n) is hiehgt of tree
            res = []
            for i in range(K): # O(n), n = len(points)
                res.append(heappop(heap)[1]) # O(log(n)), n = total nodes in tree.
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
            # UPDATED: TC = O(nlogk) + O(k) , SC: O(k)
            heap = []
            for point in points: # O(n), n = points
                e_dist = -1*self.get_distance(point[0], point[1]) # O(1)
                heappush(heap, (e_dist, point))  # O(logh).. x O(log(k))
                if len(heap) == K:
                    # Pop from heap
                    heappop(heap) # O(log(k))
            res = []

            for i in heap:  # O(K)
                res.append(i[1])  # O(1)
#                 res.append(heappop(heap)) # O(log(k)) fast if sorted order is required
            return res

    def get_distance(self, p_0, p_1):
        return (p_0**2 + p_1**2) ** 0.5


a = Solution()
a.kClosest([[1,3],[-2,2]], 1)
