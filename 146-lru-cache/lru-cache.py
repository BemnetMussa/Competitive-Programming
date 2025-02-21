class Node:
    def __init__(self,key=0, value=0,next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node):
        previous_node = self.tail.prev
        previous_node.next = node
        node.prev = previous_node
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self,node):
        previous_node = node.prev
        previous_node.next = node.next
        node.next.prev = previous_node
    
    def getHead(self):
        return self.head.next


class LRUCache:

    def __init__(self, capacity: int):
        self.order = LinkedList()
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.order.remove(node)
        self.order.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.order.remove(node) 
            self.order.add(node)
        else:
            if self.capacity == len(self.cache):
                head = self.order.getHead()
                self.order.remove(head)
                self.cache.pop(head.key)
            node = Node(key,value)
            self.order.add(node)
            self.cache[key] = node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
