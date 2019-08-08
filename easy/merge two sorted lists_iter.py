# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # If either are empty lists
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        # If both have size 1
        if l1.next is None and l2.next is None:
            if l1.val <= l2.val:
                l1.next = l2
                return l1
            else:
                l2.next = l1
                return l2

        # Otherwise
        # Set preliminary positions
        curr1 = l1
        curr2 = l2
        if l1.val <= l2.val:
            smaller = l1
            if l1.next is not None:
                curr1 = l1.next
            else:
                curr1.next = l2
                return smaller
        else: 
            smaller = l2
            if l2.next is not None:
                curr2 = l2.next
            else: # Its automatically smaller list
                curr2.next = l1
                return smaller
        new_head = smaller
        while curr1 is not None and curr2 is not None:
            # If list 1 has smaller node
            # Make smaller element point to the new smaller element
            # i.e. list 1 and increment
            if curr1.val <= curr2.val:
                smaller.next = curr1
                smaller = smaller.next
                curr1 = curr1.next
            # Vice versa
            else:
                smaller.next = curr2
                smaller = smaller.next
                curr2 = curr2.next

        # Handle case when either list is longer
        if curr1 is None and curr2 is not None:
            smaller.next = curr2
        elif curr1 is not None and curr2 is None:
            smaller.next = curr1

        return new_head
