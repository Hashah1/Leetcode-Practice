# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.res = None  # Resulting linked list
        self.tail = None
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # If l1 is null, check if l2 exists. If so, append l2
        if not l1:
            if l2:
                if self.res:
                    self.tail.next = l2
                else:
                    self.res = l2
            return self.res
        if not l2:
            if l1:
                if self.res:
                    self.tail.next = l1
                else:
                    self.res = l1
            return self.res



        if self.is_less_than(l1,l2):
            node = ListNode(l1.val)

            if not self.res:
                self.res = node
                self.tail = node
            else:
                # Append to linked list and increment tail
                self.tail.next = node
                self.tail = self.tail.next
            self.mergeTwoLists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            if not self.res:
                self.res = node
                self.tail = node
            else:
                # Append to linked list and increment tail
                self.tail.next = node
                self.tail = self.tail.next
            self.mergeTwoLists(l1, l2.next)
        return self.res

    @staticmethod
    def is_less_than(l1, l2):
        # Returns true if l1 <= l2
        return True if l1.val <= l2.val else False


