class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexity: O(len(digit) ^ len(digits))
        Space Complexity:
        """
        graph = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        all_combos = []
        cur_str = ""
        def dfs(cur_str, digits):
            if not digits:
                all_combos.append(cur_str)
                return
            for char in graph[digits[0]]:
                dfs(cur_str + char, digits[1::])

        dfs("", digits)
        return all_combos if digits else ""