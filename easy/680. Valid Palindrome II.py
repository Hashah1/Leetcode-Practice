class Solution:
    def validPalindrome(self, s: str) -> bool:
        """TC = O(len(s))"""
        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # Check to see if we remove ith index, the rest
                # of inner string is palindrome
                if is_palindrome(i + 1, j): i += 1
                # Vice versa
                elif is_palindrome(i, j - 1): j -= 1
                else:
                    return False

        return True