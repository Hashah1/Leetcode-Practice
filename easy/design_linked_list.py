class Node(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        node = self.help_get_node(index)
        if not node:
            return -1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)  # Create node with value
        node.next = self.head  # Point to head
        self.head = node  # Update head

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        # If list is empty
        if not self.head:
            self.addAtHead(val)
            return
        node = Node(val)
        # Get tail node.
        ptr = self.get_tail(self.head)
        ptr.next = node  # Add tail

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
            return
        p1 = self.help_get_node(index - 1)
        if not p1:  # Invalid index
            return
        # Insert as normal
        new_node = Node(val)
        p2 = p1.next
        new_node.next = p2
        p1.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
            return
        p1 = self.help_get_node(index)
        if not p1: # Invalid index
            return
        p2 = self.help_get_node(index - 1)
        if not p2: # Invalid index
            return
        p2.next = p1.next

    # Helper functions to do the specified job
    def help_get_node(self, index):
        """Finds the node and returns it"""
        p1 = self.head
        for i in range(index):
            if p1:
                p1 = p1.next
            else:
                break
        return p1

    @staticmethod
    def get_tail(ptr):
        while ptr and ptr.next:
            ptr = ptr.next
        return ptr