class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # phase I: Detect if there's a cycle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break  # Cycle detected

        # If there is no cycle, return None
        if not fast or not fast.next:
            return None

        # phase II: Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
