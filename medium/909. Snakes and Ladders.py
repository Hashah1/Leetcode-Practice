class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        BFS Approach. O(n^2) = SC = TC
        Preprocess the given board by converting it to a 1D array starting from i=1 index.
        Create a visited array of same length

        bfs on i=1 and accordingly traverse the 1d array until end is reached accordingly.
        """
        def convert(board):
            flattened = []
            r = len(board) - 1
            c = 0
            l_to_r = True # Starting direction
            while r > -1:
                while c < len(board) and c > -1:
                    # Add value to the flat board
                    flattened.append(board[r][c])
                    if l_to_r:
                        c += 1
                    else:
                        c -= 1
                if c == len(board):
                    c -= 1
                else:
                    c += 1
                l_to_r = not l_to_r # Flip dir
                r -= 1
            return flattened

        flattened_board = convert(board)
        visited = set()

        # BFS on flattened board
        q = deque([(0, 0)]) # (cur_val, min_dist) pair node in queue
        visited.add(0)
        print(flattened_board)
        while q:
            cur_idx, cur_dist = q.popleft()
            # If we reach last element in board, return the distance
            if cur_idx == len(flattened_board) - 1:
                return cur_dist

            for i in [1,2,3,4,5,6]:
                next_ = i + cur_idx
                # Only visit if not visited before
                if next_ < len(flattened_board) and next_ not in visited:
                    dst_val = flattened_board[next_]
                    visited.add(next_)
                    # Add that node to the queue
                    node = None
                    if flattened_board[next_] != -1:
                        node = (flattened_board[next_] - 1, cur_dist + 1)
                    else:
                        node = (next_, cur_dist + 1)
                    q.append(node)


        return -1


