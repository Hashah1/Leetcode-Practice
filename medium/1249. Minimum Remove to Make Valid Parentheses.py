class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Time Complexity: O(len(s))
        Space Complexity: O(1)
        """
        # Go left to right
            # update ( parenth count and ) parenth count
            # If ( < ) then delete that idx'd element
            # If not, then move to next slot
        # Go right to left:
            # update ( parenth count and ) parenth count
            # if ) < ( then delete that element
            # move to next slot
        sb = []
        i = 0
        open_brack = 0
        close_brack = 0
        while i < len(s) and s:
            char = s[i]
            if char == '(':
                open_brack += 1
            if char == ')':
                close_brack += 1
            if open_brack < close_brack:
                # Delete
                s = s[:i] + s[i + 1:]
                close_brack -= 1
            else:
                i += 1
        i = len(s) - 1
        open_brack = 0
        close_brack = 0
        while i >= 0 and s:
            char = s[i]
            if char == '(':
                open_brack += 1
            if char == ')':
                close_brack += 1
            if close_brack < open_brack:
                # Delete
                s = s[:i] + s[i + 1:]
                open_brack -= 1
            i -= 1
        return s