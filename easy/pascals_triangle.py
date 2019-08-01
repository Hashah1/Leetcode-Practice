class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 2-D List rows by columns containing the pascal triangle values
        # Pre-populate with the first two rows since they will always be the same
        res = [
            [1],
            [1,1]
        ]
        if numRows < 3:
            return res[:numRows]

        def helper(res, row, col):
            """Creates a pascal triangle 2D Array"""

            if row == col:  # We've reached end of the row
                res[row].append(1)
                row += 1
                col = 0
            if row == numRows:
                return res
            if col == 0:  # We're at the first item of the row
                res.append([1])  # Add the lead number
                col += 1

            # Recurrence relation
            relation = res[row - 1][col - 1] + res[row - 1][col ]
            # Append to the list
            res[row].append(relation)
            col += 1
            helper(res, row, col)

        helper(res, 2, 0)
        return res