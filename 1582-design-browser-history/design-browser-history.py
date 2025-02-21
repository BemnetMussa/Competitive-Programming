class Node:
    def __init__(self, value="",next=None, prev=None):
        self.val = value
        self.next = next
        self.prev = prev
      

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        self.head = Node()
        self.tail = Node()

        self.head.next = self.curr
        self.curr.prev = self.head
        self.curr.next = self.tail
        self.tail.prev = self.curr
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        
        self.curr.next = new_node
        new_node.prev = self.curr
        new_node.next = self.tail
        self.tail.prev = new_node

        self.curr = new_node
        temp = self.head
     
  

    def back(self, steps: int) -> str:
        
        while steps > 0 and self.curr.prev.prev:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val
        

    def forward(self, steps: int) -> str:
 
        while steps > 0 and self.curr.next.next:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)