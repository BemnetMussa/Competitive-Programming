'''


'''

class Solution:
    def decodeString(self, s: str) -> str:
        # 3[a]2[bc]

        stack = []
        current_str = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char) # 1 upto 9 but 10[...]
            elif char == "[":
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == "]":
                prev_str, prev_num = stack.pop()
                current_str = prev_str + current_str * prev_num

            else:
                current_str += char

        return current_str


        