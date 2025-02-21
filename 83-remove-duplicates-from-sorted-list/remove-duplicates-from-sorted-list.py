class Solution:
    def deleteDuplicates(self, head):
        new = ListNode(0) 
        dummy = new  

        unique = []  # List to keep track of unique values

     
        while (head != None):
            if not(head.val in unique):  
                unique.append(head.val)  # 
            head = head.next 

        for i in unique:
            dummy.next = ListNode(i)  # Create a new node for each unique value
            dummy = dummy.next  # Move the dummy pointer to the new node

        dummy = None  # Set dummy to None (not necessary)

        return new.next  # Return the modified list starting from the first real node
