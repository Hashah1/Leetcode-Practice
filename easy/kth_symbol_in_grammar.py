# Failed test case
# 30
# 434991989
class Solution(object):
    def __init__(self):
        self.prev_row = "0"

    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)/2)
        # # Row starts from 2 since first row is already taken
        # row = 2
        # index = 0
        #
        # def build_row(modded_row, row, index):
        #     """Builds our row and respective indices"""
        #     # Length of each row can't be >= 2^(row - 1)
        #     cap = pow(2, row - 1)
        #     if index >= cap - 1:
        #         # Next row's time
        #         row += 1
        #         # Update the previous row
        #         self.prev_row = bin(modded_row)
        #         # Set current row and index for the next round
        #         modded_row = 0
        #         index = 0
        #     # If the desired row has been reached, return answer.
        #     if row > N:
        #         return self.prev_row[K - 1]
        #     # Replace 0 with 01 and 1 with 10
        #     if self.prev_row[index] == "0":
        #         # modded_row += "0"
        #         # modded_row += "1"
        #         modded_row += 1
        #     else:
        #         # modded_row += "1"
        #         # modded_row += "0"
        #         modded_row += 2
        #
        #     # Recurse with increamented index
        #     return build_row(modded_row, row, index + 1)
        # return int(build_row(0, row, index))


if __name__ == '__main__':
    a = Solution()
    b = a.kthGrammar(4,8)
    pass
