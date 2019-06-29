# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def isPalindrome(self, head):
    #     """ O(n) space complexity
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     # Create stack
    #     stk = []
        
    #     node = head
    #     while node:
    #         stk.append(node.val)
    #         node = node.next
    #     node = head
    #     while stk:
    #         a = stk.pop()
    #         if node.val != a:
    #             return False
    #         node = node.next
    #     return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Get middle of the linked list.
        slow = head
        curr = head
        while curr and curr.next:
            slow = slow.next
            curr = curr.next.next
        new_head = self.reverse(slow)

        # Compare first half and second half
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True
    
    def reverse(self, head):
        """
        Reverse second half of linked list
        """
        new_head = None
        c = head
        while c:
            n = c.next # Have a forward reference
            c.next = new_head # Reverse the connection
            # Move up the new references
            new_head = c 
            c = n
        return new_head