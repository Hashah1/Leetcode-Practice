class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Thought process:
        TC: O(len(numRows)), SC = O(matrix)

        - Create rows with length of numRows
        - Loop through all char in s:
            if first or last row is reached, toggle whether to go down or zigzag up
            add to each str in row. No need to create an extra col since we're dealing with strings
            and add on of char can be treated as a 'new col'
        """
        if numRows <= 1:
            return s
        all_rows = ['' for i in range(numRows)]
        row = 0
        zigzag = True
        # Build matrix of zigzag repr of s
        for idx, char in enumerate(s):
            # Toggle zigzag
            if row == 0 or row == numRows - 1:
                zigzag = not zigzag
            all_rows[row] += char
            if zigzag:
                row -= 1
            else:
                row += 1

        # Return string repr of zigzag matrix
        return ''.join(row for row in all_rows)