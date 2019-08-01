class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow_pos(x, n):
            if n == 0:
                return 1
            # Bubble down to the smallest num
            half_prod = pow_pos(x, int(n / 2))

            # If power is odd,
            # Multiply num with half of the product^2
            if n % 2:
                return half_prod * half_prod * x
            else:  # If even, simply return the prod^2
                return half_prod * half_prod
        res = pow_pos(x,abs(n))
        return 1/res if n < 0 else res