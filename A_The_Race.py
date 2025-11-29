

s, v1, v2, t1, t2 = map(int, input().split())

first_time = t1 + (v1 * s) + t1
second_time = t2 + (v2 * s) + t2

if first_time < second_time:
    print("First")
elif first_time > second_time:
    print("Second")
else:
    print("Friendship")
