from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        TC: O(len(S) * log(S))
        SC: O(len(S))
        """
        freq_table = collections.Counter(S)
        heap = []
        # Convert to a heap
        for k, v in freq_table.items():
            heappush(heap, (-v, k))

        # If max count is > half of the string then impossible
        if -heap[0][0] > (len(S) + 1)/2: return ""

        # Reorganize string
        res = []
        while len(heap) >= 2:
            first_count, first_char = heappop(heap)
            sec_count, sec_char = heappop(heap)
            if not res or first_char != res[-1]:
                res.append(first_char)
                res.append(sec_char)
            elif not res:
                res.append(sec_char)
                res.append(first_char)

            if first_count + 1 != 0:
                heappush(heap, (first_count + 1, first_char))
            if sec_count + 1 != 0:
                heappush(heap, (sec_count + 1, sec_char))
        return ''.join(res) + (heap[0][1] if heap else "")
