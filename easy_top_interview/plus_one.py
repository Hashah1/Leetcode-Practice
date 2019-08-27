class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while True:
            carry = self.get_carry(digits[i])
            digits[i] += 1
            if carry:
                digits[i] = 0
                i -= 1
                if i < 0:
                    digits.insert(0,0)
                    i = 0
            else:
                break


    def get_carry(self, digit):
        """Gets the carry from adding 1 to the digit.
        If no carry, return 0"""
        return 1 if digit + 1 > 9 else 0

a = Solution()
a.plusOne([9])