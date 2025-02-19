class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0  # Track size for optimized operations

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:  # Out of bounds check
            return -1

        temp = self.dummy.next
        for _ in range(index):
            temp = temp.next

        return temp.val if temp else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1  # Update size

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        itr = self.dummy

        while itr.next:
            itr = itr.next

        itr.next = new_node
        self.size += 1  # Update size

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # Out of bounds check
            return

        new_node = Node(val)
        itr = self.dummy
        counter = 0
        
        # Traverse to the node before the desired index
        while counter < index:
            itr = itr.next
            counter += 1

        # Insert the new node
        new_node.next = itr.next
        itr.next = new_node

        self.size += 1  # Update size

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # Out of bounds check
            return

        itr = self.dummy
        counter = 0

        # Traverse to the node before the target index
        while counter < index:
            itr = itr.next
            counter += 1

        # Delete the node by skipping it
        itr.next = itr.next.next

        self.size -= 1  # Update size
