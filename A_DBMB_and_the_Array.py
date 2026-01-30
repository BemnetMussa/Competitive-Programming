
def check_(array, s, x):
    total = sum(array)
    reminder_ = s % total 

    if reminder_ > s:
        return print("No")
    
    needed_ = x % reminder_

    if needed_ > x:
        return print("No")
    
    return print("Yes")

test_cases = int(input())
for i in range(test_cases):
    n, s, x = map(int, input().split())
    array = list(map(int, input().split()))
    
    check_(array, s, x)


