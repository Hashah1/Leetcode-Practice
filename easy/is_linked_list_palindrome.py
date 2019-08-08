# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # If length of list is 0 or 1, return True
        if not head or not head.next:
            return True
        # Step 1: Find middle node
        mid_node = self.get_mid_node(head)
        # Step 2: Reverse first half of the list
        new_head = self.reverse_list(mid_node)
        # Compare the two halves and return True if equal
        while head and new_head:
            if new_head.val != head.val:
                return False
            new_head = new_head.next
            head = head.next
        return True

    def get_mid_node(self, node):
        """
        Returns middle node of the list
        """
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, node):
        """
        Reverses the list.
        """
        if not node.next:
            return node
        # Get the last element, this will be the new head
        new_head = self.reverse_list(node.next)
        node.next.next = node
        node.next = None
        return new_head
a = Solution()
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
# head.next.next.next = ListNode(1)
a.isPalindrome(head)