class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity: O(len(board) * len(board[0]))
        Space Complexity: O(1)
        """
        def dfs(row, col, word): # TODO: Look onto how these funcs work
            # Base Case
            if word == "":
                return True
            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) or board[row][col] != word[0]:
                return False

            board[row][col] = "0" # Mark visited
            found = False
            for r, c in neighbors:
                found = dfs(row + r, col + c, word[1:])
                if found:
                    break
            board[row][col] = word[0]
            return found

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        is_valid = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    is_valid = dfs(row, col, word)
                    if is_valid:
                        return True
        return is_valid