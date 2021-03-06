class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 2-D List rows by columns containing the pascal triangle values
        # Pre-populate with the first two rows since they will always be the same
        res = [
            [1],
            [1,1]
        ]
        if rowIndex < 2:
            return res[rowIndex]

        def helper(res, row, col):
            """Creates a pascal triangle 2D Array"""

            if row == col:  # We've reached end of the row
                res[row].append(1)
                row += 1
                col = 0
            if row > rowIndex:
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
        return res[rowIndex]

if __name__ == "__main__":
    a= Solution()
    a = a.getRow(4)
    pass