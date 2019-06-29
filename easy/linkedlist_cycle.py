# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """ 
        fast = slow = head
        # Iterate until two pointers cross path.
        while fast and fast.next:
            # For every slow pointer iteration, 
            # iterate fast ptr two places.
            # They are bound to meet if there's a cycle.
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False