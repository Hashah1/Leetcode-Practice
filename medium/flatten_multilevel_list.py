"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        parents_stk = []
        cur = head

        while parents_stk or cur:
            if cur.child:
                # Push the parent to stack
                parents_stk.append(cur)
                cur = cur.child
            if not cur.next:
                # Pop the parent off from stack
                if not parents_stk:
                    break
                # Get parent and its next value
                parent = parents_stk.pop()
                lead = parent.next
                
                # Connect sub-level end to parents next node
                cur.next = lead
                if lead:
                    lead.prev = cur
                    
                # Connect parent to child
                parent.next = parent.child
                parent.next.prev = parent
                parent.child = None
            if not cur.child:
                cur = cur.next
        return head