# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Strategy: linear time complexity
        Go to the end of the linked list via recursion
        Oncee reached end return 2*i if node is 1 else return 0
        """
        def helper(node):
            if not node.next: # Reached end of thee linked list
                if node.val == 1:
                    return 2**0, 0
                return 0, 0
            ret, idx = helper(node.next)
            idx += 1
            if node.val == 1:
                return 2**idx + ret, idx
            else:
                return ret, idx
        return helper(head)[0]