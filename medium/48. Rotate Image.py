class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def reverse(lst):
            l = 0
            r = len(lst) - 1
            while l < r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
            return lst
        # Transpose each row in matrix
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        # Reverse each matrix row
        for row in range(len(matrix)):
            matrix[row] = reverse(matrix[row])
        return matrix

