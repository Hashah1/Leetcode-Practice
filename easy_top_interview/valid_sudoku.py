class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check to see if case 1 and case 2 is satisfied
        for column in range(len(board)):
            row_list, col_list = [], []
            for row in range(len(board)):
                row_list.append(board[column][row])
                col_list.append(board[row][column])
            # Check if the row and columns are unique
            if not self.is_unique(row_list) or not self.is_unique(col_list):
                return False

        # Check to see if case 3 is satisfied
        box = []
        row = column = start = 0
        total_size = len(board[0]) * len(board)
        curr_iter = 0
        while curr_iter < total_size:
            box.extend(board[row][column])
            if (column + 1) % 3 is 0: # Restart box from row 0 but to the right
                if (row + 1) % 3 is 0:
                    if not self.is_unique(box):
                        return False
                    else:
                        box = []
                if row >= len(board) - 1:
                    row = 0
                    start = column + 1
                else:  # Move to the next line
                    row += 1
                column = start
            else:
                column += 1
            curr_iter += 1
        return True

    def is_unique(self, nums):
        freq = set()
        for i in nums:
            if i != '.' and i in freq:
                # Update the count in dictionary
                return False
            else:
                freq.add(i)
        return True