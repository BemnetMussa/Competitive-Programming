class Solution:
    def minimumSteps(self, s: str) -> int:
        white_pos = 0
        steps = 0

        for current_pos, char in enumerate(s):
            
            if char == "0":
              
                steps += current_pos - white_pos
                white_pos += 1

        return steps