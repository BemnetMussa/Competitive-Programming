# class Solution:
#     def isPalindrome(self, x: int) -> bool:
        
#         y = x 
#         r = 0
#         while y > 0:
#             rm = y % 10 
#             r = (r * 10 + rm)
#             y = y//10


#         return True if y == x else False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # Copy the input number to another variable
        original = x  # Save the original number
        reversed_number = 0  # Initialize the reversed number

        # Reverse the digits of the number
        while x > 0:
            digit = x % 10  # Get the last digit
            reversed_number = reversed_number * 10 + digit  # Add the digit to the reversed number
            print(reversed_number)
            x = x // 10  # Remove the last digit from x

        # Compare the reversed number with the original number
        return reversed_number == original
