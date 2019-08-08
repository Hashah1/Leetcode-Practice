# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Approach:
        # 1. Get lenght of both lists
        # 2. Iterate the longer list times (difference of lenA and lenB). So they start from same spots.
        p_a = headA
        p_b = headB
        l_a, l_b = self.get_list_lengths(p_a, p_b)

        # Make ptr for list A and list B start from a point so that
        # both can reach None at the same time or reach the intersection node at same time.
        if l_a > l_b:
            # If list A is greater than list B
            diff = l_a - l_b
            i = 0
            while i != diff and p_a:
                p_a = p_a.next
                i += 1
        elif l_b > l_a:
            diff = l_b - l_a
            i = 0
            while i != diff and p_b:
                p_b = p_b.next
                i += 1

        # Simply return true if node is the same or not
        while True:
            if not p_a:
                return None
            if not p_b:
                return None
            if p_a == p_b:
                return p_a
            p_a = p_a.next
            p_b = p_b.next

    @staticmethod
    def get_list_lengths(p_a, p_b):
        """Gets lengths of both lists"""
        l_a = 0
        l_b = 0
        while True:
            if p_a:
                p_a = p_a.next
                l_a += 1
            if p_b:
                p_b = p_b.next
                l_b += 1
            if not p_a and not p_b:
                break
        return l_a, l_b