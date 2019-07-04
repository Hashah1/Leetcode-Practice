class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        for each in S:
            # Add to stack, if its a duplicate 
            # with the top most val, remove the two 
            # val and add current val
            if stack and each is stack[-1]:
                stack.pop()
                continue

            stack.append(each)

        return ''.join(stack)

if __name__ == "__main__":
    a = Solution()
    a = a.removeDuplicates("heeeeellloomyfriiiend")
    pass