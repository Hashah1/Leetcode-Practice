class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Hold list of palindromic substrings
        valid_palindromes = []
        for left_offset in range(len(s)):
            for right_offset in reversed(range(len(s))):
                if left_offset <= right_offset:
                    palindrome = s[left_offset:right_offset + 1]
                    if self.is_valid_palindrome(palindrome):
                        valid_palindromes.append(palindrome)
                else:
                    break
        return len(valid_palindromes)

    def is_valid_palindrome(self,s):
        return True if s[::] == s[::-1] else False
