class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # Convert list to deque for efficient pops from both ends
        queNums = deque(nums)

        def game(arr, player1, player2, turn):
            # base case 
            if not arr:
                return player1 >= player2

            # Option 1: Player picks the leftmost number
            left_val = arr.popleft() 
            if turn:  
                win_left = game(arr, player1 + left_val, player2, not turn)
            else:     
                win_left = game(arr, player1, player2 + left_val, not turn)

            arr.appendleft(left_val) 

            # Option 2: Player picks the rightmost number
            right_val = arr.pop()  
            if turn:  
                win_right = game(arr, player1 + right_val, player2, not turn)
            else: 
                win_right = game(arr, player1, player2 + right_val, not turn)
            arr.append(right_val)  


            if turn:
                return win_left or win_right
            else:
                return win_left and win_right

        return game(queNums, 0, 0, True)
