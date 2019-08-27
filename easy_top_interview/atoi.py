class Solution:
    def myAtoi(self, str: str) -> int:
        res = ''
        number_started = False
        # Check if each element is a -/+
        # If it is, then assign it to a string
        # Everything after that is added, unless a non-digit is noticed.
        for char in str:
            # If an alphabet or a '.' comes, break
            if char.isalpha() or char == '.':
                break
            # If number has already started and we face something like '+-12', break
            elif number_started and (char == ' ' or char == '-' or char == '+'):
                break
            # If char is a digit or beginning with +/-, add to res and mark number beg.
            if char.isdigit() or char == '-' or char == '+':
                number_started = True
                res += char
        try:
            # Try converting res to an int version.
            res = int(res)
            # If successful, check bounds
            if res > 2**31 - 1:
                res = 2**31 - 1
            elif res < -2**31:
                res = -2**31
        except Exception:
            # In case res = ''
            res = 0
        return res
