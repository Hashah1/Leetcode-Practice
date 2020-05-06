class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = y_x = 0
        xy_swaps = yx_swaps = 0
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                x_y += 1
            if s1[i] == "y" and s2[i] == "x":
                y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1
        xy_swaps += x_y // 2 + x_y % 2
        yx_swaps += y_x // 2 + y_x % 2
        return xy_swaps + yx_swaps