# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = None
        it1 = head
        while it1:
            i = 0
            tmp = it1
            while i != n:
                tmp = tmp.next
                i += 1
            if tmp:
                prev = it1
                it1 = it1.next
            elif not tmp:  # If tmp is null, we've found the nth last element
                if it1 == head:
                    head = head.next
                else:
                    prev.next = it1.next
                return head