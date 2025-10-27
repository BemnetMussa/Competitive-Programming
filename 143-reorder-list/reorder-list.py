# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Given: given a singly linked list. can be repreasted as 0 -> 1 -> 2 -> 3
reodrer it to have 0 -> 3 => 1 => 2

head = [1,2,5,3,4]
1 -> 4 -> 2 -> 3

since it is a singly linked list. 
half [1, 2]
rest_half [3, 4] # need to be reversed
        [4, 3]

1 -> 4 -> 2 -> 3

haflf and rest_half -> (reverse the rest of the half)
updating the head with the given values

1 -> 2 -> 3 -> 4 -> 5 -> 6
first half 1 -> 2 -> 3 

slow = 4 -> 5 -> 6
4 -> None

6 -> 5 -> 4
1 -> 2 -> 3

1 -> 6 -> 2
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # step 1: finding the half using (fast and slow pointer)
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev, curr = None, slow.next
        slow.next = None # disconnecting the first half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge the first and second half
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        
            


        
