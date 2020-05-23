class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity:
            O(len(A) + len(B))
        Space Complexity:
            O(len(A) + len(B))
        """
        if not A or not B:
            return []
        def merge(interval_a, interval_b):
            beg_a, end_a = interval_a
            beg_b, end_b = interval_b
            merge_beg = max(beg_a, beg_b)
            merge_end = min(end_a, end_b)
            # Merge only valid interval
            if merge_beg <= merge_end:
                interval = [merge_beg, merge_end]
                result.append(interval)
            return

        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            merge(A[i], B[j])
            a_end = A[i][1]
            b_end = B[j][1]
            if a_end < b_end:
                # Then move to the next interval in A
                # since A can potentially have another interval
                # which lies within current b_end
                i += 1
            else:
                j += 1

        return result