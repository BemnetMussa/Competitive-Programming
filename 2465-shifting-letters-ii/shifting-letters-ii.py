class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        '''
        Given:
            s: given string
            shifts[[int]] = [[start, end, directions]]

        for every shfit in shifts
            if directions = 1, shift all characters forward -> start to the end 
            if directions = 0, shfit all characters backward-> start to the end 

        goal: string after all shifts has been applied on 

        approch:
        s = "a b c", shifts = [[0,1,0],[1,2,1],[0,2,1]]
    1st ->   l r    => zac
             z a c
    2nd ->     l r  => zbd
             z b d
    3rd ->   l   r => ace

        answer = 'ace'

        constratin: 10^4 = n
                    n * n => O(n^2)
        '''

        prefix_sum = [0] * (len(s)+1)


        # mark the queries 
        for l, r, d in shifts:
            if d == 0: # backward shift
                prefix_sum[l] -= 1 # marking the start
                prefix_sum[r + 1] += 1 # marking the end
            else: # forward shift
                prefix_sum[l] += 1
                prefix_sum[r + 1] -= 1

        print(prefix_sum)
        accumlate = 0
        answer = ''
        for i, char in enumerate(s):
            char_ord = ord(char) - ord('a') # 0-25
            accumlate += prefix_sum[i]
            char_ord = (char_ord + accumlate) % 26 # 25 + 5 = 30 
            answer += chr(char_ord + ord("a"))

        return answer


