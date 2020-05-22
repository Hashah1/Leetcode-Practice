class Solution:
    def romanToInt(self, s: str) -> int:
        """Time Complexity: O(len(s)), Space Complexity: O(13)"""
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            # For subtraction cases
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        number = 0
        # Iterate till second last char
        i = 0
        while i < len(s):
            # If two chars are in mapping, subtract
            if s[i: i + 2] in mapping:
                number += mapping[s[i: i + 2]]
                i += 2
            else:
                number += mapping[s[i]]
                i += 1
        return number