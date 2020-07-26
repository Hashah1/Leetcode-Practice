
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        TC: SC: O(M*N)
        1 - For every element in first row, check its diagonal
        2 - For every eleement in first col, check its diagonal

        How to check its diagonal:
        Recurse until the last char in the diagonal. When last char is found,
        validate it.
        """
        def validate(cur_diag, row, col):
            if not (row < len(matrix)) or not (col < len(matrix[0])):
                # Out of bounds.
                return True
            if matrix[row][col] != cur_diag[-1]:
                return False
            return validate(cur_diag + [matrix[row][col]], row + 1, col + 1)
        top = True
        left = True
        for i in range(len(matrix[0])):
            top = validate([matrix[0][i]], 0, i)
            if not top:
                return False

        for i in range(len(matrix)):
            left = validate([matrix[i][0]], i, 0)
            if not left:
                return False

        return True

