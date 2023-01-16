N = int(input())
a = list(map(int,input().split()))

bonus = 1
fail = 0

for i in a:
    if i:
        fail += bonus
        bonus += 1
    else:
        bonus = 1
print(fail)