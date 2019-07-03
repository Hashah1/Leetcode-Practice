class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count_of_lp = 0
        count_of_rp = 0
        str = ""
        list_of_valid_substrings = []
        for each_char in S:
            str += each_char
            if each_char == ')':
                count_of_rp += 1
            elif each_char == '(':
                count_of_lp += 1
            
            # If count of ( and count of ) are equal, 
            # then we have a primitive substring.
            if count_of_lp is count_of_rp:
                count_of_lp = count_of_rp = 0
                list_of_valid_substrings.append(str)
                str = ""
        # Now strip off outer paranthesis of each substring
        for i in range(len(list_of_valid_substrings)):
            list_of_valid_substrings[i] = list_of_valid_substrings[i][1:-1]
        return ''.join(list_of_valid_substrings)

if __name__ == "__main__":
    a = Solution()
    b = a.removeOuterParentheses('(()())(())')
    pass