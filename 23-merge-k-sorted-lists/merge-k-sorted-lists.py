class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (node value, index, node) // included i if val is the same
        heap = []
        
        for i, linked_list in enumerate(lists):
            if linked_list:
                heappush(heap, (linked_list.val, i, linked_list))
        # print(heap)
        
        # Dummy node to 
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heappop(heap) 
            current.next = node 
            current = current.next  
            
            if node.next:  
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
