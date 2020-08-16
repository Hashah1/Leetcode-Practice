class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create bounds for the new spiral matrix
        tr = 0 # Top Row
        br = n - 1 # Bot Row
        lc = 0 # Left Col
        rc = n - 1 # Right Col
        # Create a var to keep track of the number to add
        num_to_add = 1
        dir_ = "right"
        # Create matrix prepopulated with 0s as dummy data
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while num_to_add <= n**2:
            if dir_ == "right":
                for i in range(tr, rc + 1):
                    matrix[tr][i] = num_to_add
                    num_to_add += 1
                dir_ = "down"
                tr += 1

            elif dir_ == "down":
                for i in range(tr, br + 1):
                    matrix[i][rc] = num_to_add
                    num_to_add += 1
                dir_ = "left"
                rc -= 1
            elif dir_ == "left":
                for i in range(rc, lc - 1, -1):
                    matrix[br][i] = num_to_add
                    num_to_add += 1
                dir_ = "up"
                br -=1
            elif dir_ == "up":
                for i in range(br, tr - 1, -1):
                    matrix[i][lc] = num_to_add
                    num_to_add += 1
                lc += 1
                dir_ = "right"
        return matrix