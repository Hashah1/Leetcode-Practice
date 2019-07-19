class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        # Push onto stack
        for char in s:
            if char.isalnum():
                stk.append(char.lower())
        return True if stk[:] == stk[::-1] else False
