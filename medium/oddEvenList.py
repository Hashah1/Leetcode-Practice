# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If length of list is 1 or 2, return head
        # as it's already in correct format
        if not head or not head.next or not head.next.next:
            return head
        # Have pointer to tail of the odd list which will be built.
        # So far, only head is in the odd list
        odd_list_tail = head
        # The lead ptr will scout for all odd nodes,
        # and with the help of trail ptr, add it to the odd_list
        trail = head.next
        lead = trail.next

        index = 2  # Start with odd indexed node (lead ptr)
        while lead:
            # Whenever lead is on an odd node, update the odd_list_tail
            if index % 2 == 0:  # If at odd node
                # Move node to the odd list
                trail.next = lead.next
                lead.next = odd_list_tail.next
                odd_list_tail.next = lead

                # Move the lead ptr back to its original place
                lead = trail.next
                # Update tail
                odd_list_tail = odd_list_tail.next
            else:
                # Move the lead and trail ptr
                lead = lead.next
                trail = trail.next
            index += 1
        return head