class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def helper( s, beg, end):
            if beg >= end:
                return
            # Swap first and last char
            s[beg], s[end] = s[end], s[beg]
            helper(s, beg + 1, end - 1)
        # Base case:
        helper(s, 0, len(s) - 1)