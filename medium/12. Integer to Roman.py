class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Time Complexity: O(len(symbols_list))
        Space Complexity: O(len(symbols_list))

        Create basic map of all symbols -> integers

        Create a list of all symbols in decreasing order.

        In while loop. Iterate until end of symbols list:
            if Symbol->number <= num:
                Subtract number from num
                Add symbol to result
            else:
                next idx
        """
        roman_number = ""
        mapping = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        symbols = list(mapping.keys())
        i = len(symbols) - 1
        while i >= 0:
            symbol = symbols[i]
            symbol_rep = mapping[symbol]
            if symbol_rep <= num:
                num -= symbol_rep
                roman_number += symbol
            else:
                i -= 1
        return roman_number
