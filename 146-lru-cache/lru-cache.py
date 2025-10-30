'''
Design a data structrue the follows the LRU chache.
properties LRU cahce should have
- LRUCahce(int capacity) -> define a fixed capacity
- int get(int key) -> return the value of the key if it exists otherwise *-1
- int put(key, value) -> update a value of the key if th key exsits otherwise add the key. 
            - ** if the capacity have arleady reached remove the least recently used one and replacemethods.

* must be implemented in O(1) time all of the methods.

approch: 
using linked list + map
all the operations in O(1)
'''

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.map = {}

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _addToHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._addToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._addToHead(node)
        else:
            if len(self.map) == self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.map[lru_node.key]

            new_node = Node(key, value)
            self.map[key] = new_node
            self._addToHead(new_node)



            
    
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)