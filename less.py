a, b = map(int,input().split())
T = list(map(int,input().split()))

for i in range(a):
    if T[i] < b:
        print(T[i],end=" ")