# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            if head.val == val:
                head = head.next
                prev = cur = head
                continue

            elif cur.val == val:
                prev.next = cur.next  # Delete current node
                prev = cur = head
                continue
                # continue
            # else:
            # Increment ptrs while keeping ref to previous node
            prev = cur
            cur = cur.next
        return head


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(4)

a = Solution()
a.removeElements(node, 1)