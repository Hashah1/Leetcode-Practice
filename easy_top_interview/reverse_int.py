class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = list(str(x))  # Convert to list
        # If x is negative, start from index = 1
        beg = 1 if x < 0 else 0
        end = len(x_str) - 1
        while beg <= end:
            # Swap
            x_str[beg], x_str[end] = x_str[end], x_str[beg]
            beg += 1
            end -= 1
        a = int(''.join(str(e) for e in x_str))
        # Return 0 if overflow
        return 0 if abs(a) > 2**31-1 else a
