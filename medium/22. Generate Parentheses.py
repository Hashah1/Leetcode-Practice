class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(cur_str, left, right):
            if left > n or right > left:
                return
            if len(cur_str) == n * 2:
                res.append(cur_str)
                return
            helper(cur_str + "(", left + 1, right)
            helper(cur_str + ")", left, right + 1)
        helper("", 0, 0)
        return res


