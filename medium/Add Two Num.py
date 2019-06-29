# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    carry = False
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Start at head.
        ptr_1 = l1
        ptr_2 = l2
        
        while ptr_1 and ptr_2:  # Iterate while both are not null.
            # Get the sum for each of the nodes.
            # Add it to first list's node.
            ptr_1.val = self.calc_sum(ptr_1.val, ptr_2.val)
            
            # Special cases for handling the carry out,
            # which may have been generated from addition
            if self.carry:
                # For next element, add carry.
                if ptr_1.next and ptr_2.next:
                    ptr_1.next.val += 1
                # If l1 is longer than l2
                elif ptr_1.next and not ptr_2.next:
                    new_node = ListNode(1)
                    ptr_2.next = new_node
                else:
                    # When 
                    # 1. l1,l2 are not the same size and on last node
                    # 2. l2 is longer than l1
                    new_node = ListNode(1)
                    ptr_1.next = new_node
                self.carry = False
            
            # Move to the next node.
            # Set reference to previous node for list being returned.
            tmp1 = ptr_1
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next
            
        # Case 2: If l1 is smaller than l2
        # Extend l1
        if ptr_2 and not ptr_1:
                tmp1.next = ptr_2
        return l1
        
    def calc_sum(self, t1, t2):
        # Handle addition where sum > 10
        if t2 + t1 >= 10:
            self.carry = True
        return (t1 + t2) % 10