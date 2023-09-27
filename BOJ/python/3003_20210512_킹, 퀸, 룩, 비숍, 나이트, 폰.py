chess = list(map(int, input().split(' ')))

for i in range(0,6):
    if i <= 1:
        num = 1
    elif i <= 4:
        num = 2
    elif i == 5:
        num = 8

    if chess[i] > 1:
        chess[i] = -(chess[i] - num)
    else:
        chess[i] = num - chess[i]

for result in chess:
    print(result, end=' ')
