sum = 0
for i in range(5):
    number = int(input())
    if number > 40:
        sum += number
    else:
        sum += 40
print(sum//5)