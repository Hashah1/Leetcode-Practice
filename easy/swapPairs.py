# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If no item in list
        if not head:
            return
        # If one item in list
        if head and not head.next:
            return head

        # Swap the two node values
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(head.next.next)
        return head