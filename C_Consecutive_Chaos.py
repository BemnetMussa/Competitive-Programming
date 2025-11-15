s = input()

turn = 1

stack = []
for char in s:
    if stack and stack[-1] == char:
        stack.pop()
        turn += 1
    else:
        stack.append(char)

print("Yes" if turn % 2 == 0 else "No")