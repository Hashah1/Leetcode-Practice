class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """
        TC: O(size of M)
        SC: O(size of M)
        DP Approach
        Create 2d dp matrix.
        DP(i, j) = A list containing max lengths in each direction (H, V, D, AD)
        Recurrence relation:
        if val == 1:
            Update the DP tuple at i, j with max lengths in each direction so far
            Update the max result so far
        else:
            Move on...
        return max result
        Note:
        Size of DP table row will be len(M_num_cols) + 2. Leaving room to check for diagonals and antidiagonals
        """
        if not M:
            return 0
        dp = [[[0, 0, 0, 0] for col in range(len(M[0]) + 2)] for row in range(len(M) + 1)]
        max_res = 0
        for row in range(1, len(dp)) :
            for col in range(1, len(dp[0]) - 1):
                if M[row - 1][col - 1] == 1:
                    #  Update dp
                    max_hor = dp[row][col - 1][0] + 1
                    max_ver = dp[row - 1][col][1] + 1
                    max_diag = dp[row - 1][col - 1][2] + 1
                    max_antidiag = dp[row - 1][col + 1][3] + 1

                    new_add = [max_hor, max_ver, max_diag, max_antidiag]
                    for k in range(4):
                        dp[row][col][k] = max(dp[row][col][k], new_add[k])
                        max_res = max(dp[row][col][k], max_res)

        return max_res
