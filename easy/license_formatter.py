class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ""
        i = len (S) - 1
        count = 0  # Record char count for comparison with K.
        # Loop through string backwards
        while i >= 0:
            val = S[i].upper()
            if val == '-':
                # Move on to next (i - 1)th value
                i -= 1
            else:
                # If we have group of K characters
                if count == K and count != 0:
                    # Insert the value at 0th pos of res
                    res = '-' + res
                    # Reset the count
                    count = 0
                else:  # If any other character is encountered
                    # Insert to the result
                    res = val + res
                    # Increment count
                    count += 1
                    i -= 1


            
if __name__ == "__main__":
    a = Solution()
    a = a.licenseKeyFormatting("5F3Z-2e-9-w", 4)
    pass