# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # colliding pointers Approche

        # step 1: getting the length
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # step 2: getting the half
        half = length // 2

        # step 3: getting the two halfs heads 
        second_half = head
        i = 1
        while i <= half:
            second_half = second_half.next
            i += 1
    
        first_half = self.reverse(head, half)
        
        # step 4: colliding pointers
        max_sum = 0
        while first_half and second_half:
            zsum = first_half.val + second_half.val
            max_sum = max(max_sum, zsum)
            first_half = first_half.next
            second_half = second_half.next


        return max_sum # time complexity O(n) and space Compolexity O(1)


    def reverse(self, head, k):
        prev = None
        curr = head

        while k > 0 and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

            k -= 1
            
        head.next = curr
        return prev