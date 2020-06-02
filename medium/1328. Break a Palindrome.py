class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        TC = O(len(palindrome))
        SC = O(len(palindrome)) # Slicing
        Start with bounds to left and right of string:
            Either
                1.- Change first non a to a
                2.- Change last char which is a to b
                3.- Don't change middle char
            Simplified:
                Change first non-a which isnt middle char to b, return
                Change last char
        """
        if len(palindrome) == 1:
            return ""
        left = 0
        right = len(palindrome) - 1
        while left < len(palindrome) and right >= 0:
            # Change first non a char which isnt middle node.
            if left != right and palindrome[left] != 'a':
                palindrome = palindrome[:left] + 'a' + palindrome[left + 1:]
                return palindrome
            left += 1
            right -= 1
        # Nothing has been changed so far, so just change last character
        palindrome = palindrome[:left - 1] + 'b'
        return palindrome