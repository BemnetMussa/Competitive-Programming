'''
Design a circular queue. 
- a circular queue. 
- One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful. --> front of the queue. 
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

1, 2, 3, 4, 5
deQueue() -> 1 -> updated 2, 3, 4, 5 ( in an efficnt way logn or O(1) if possible )
- problem with the array is freed space must be filled so all the leemt will be shifted -> O(n)

it is possible to use many additional things liek hashmaps to store the values soething i woudn't say it is impossible but for know
just using Linked List will be better it is simple and intutive to explain. 

 2 -> 3 -> 4 -> 5
 |              |
deQueue() = shift the front head to the next one (O(1))
enQueue() = shift the rear pointer to the new value and add it (O(1)) --> **Doubly linked list
Front(), Rear() = O(1)
isEmpthy() = if fornt and rear points to each others then None then empthy otherwise False
isFull() = keeping track of the capacity wehn we add and delete **additional info needed


O(1) for all of th eoperations Valid effient

1 -> 2 -> 3 -> 4 
|              |          5

1 -> 2 -> 3 -> 4 -> 5 -> rear
|              |          
'''
# Doubly Linked List
class LinkedList:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = None
        self.prev = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.front = LinkedList()
        self.rear = LinkedList()

        # connect both - circular 
        self.front.nxt = self.rear
        self.rear.prev = self.front

        # track the length
        self.length = 0
        self.k = k # capacity

    def enQueue(self, value: int) -> bool:
        new_node = LinkedList(value)
        if self.length == self.k:
            return False

        if self.length != 0:
            self.rear.prev.nxt = new_node
            new_node.prev = self.rear.prev

            self.rear.prev = new_node
            new_node.nxt = self.rear

        else:
            self.front.nxt = new_node
            new_node.prev = self.front

            self.rear.prev = new_node
            new_node.nxt = self.rear

        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front.nxt = self.front.nxt.nxt
        self.front.nxt.prev = self.front
        self.length -= 1

        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.nxt.val
        
    def Rear(self) -> int:
        
        if self.isEmpty():
            return -1
        return self.rear.prev.val
        
    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.length == self.k:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()