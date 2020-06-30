class Solution:
    def longestMountain(self, A: List[int]) -> int:
        """
        TC: O(len(A))
        SC: constant
        """
        mtn_start = 0
        longest_mtn = 0
        while mtn_start < len(A):
            # For each mountain start, find the largest poteential mtn
            cur_mtn_end = mtn_start
            # Found poteential start, and get to the peak
            potential_mtn_discovered = False
            mtn_found = False
            while cur_mtn_end + 1 < len(A) and A[cur_mtn_end] < A[cur_mtn_end + 1]:
                # Go to next end
                cur_mtn_end += 1
                potential_mtn_discovered = True

            if potential_mtn_discovered: # If potential mtn has been discovered
                # At this point, we're at peak. Find next low if its available
                while cur_mtn_end + 1 < len(A) and A[cur_mtn_end] > A[cur_mtn_end + 1]:
                    cur_mtn_end += 1
                    mtn_found = True

            if mtn_found:
                # Update answer if proper mountain is discovered.
                longest_mtn = max(longest_mtn, cur_mtn_end - mtn_start + 1)
            # Update the starting point. Inc mtn start if no mountain is found
            mtn_start = max(cur_mtn_end, mtn_start + 1)
        return longest_mtn