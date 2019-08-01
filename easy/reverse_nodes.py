# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.next = None
        self.val = x

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        # Reverse the nodes.
        head.next.next = head
        head.next = None
        # Return the last element as the new head.
        return new_head
