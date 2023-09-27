num_list = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6, 4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1, 9, 1]]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a_mod = a % 10
    if a_mod == 1 or a_mod == 5 or a_mod == 6:
        print(a_mod)
        continue
    elif a_mod == 0:
        print(10)
        continue
    elif b % 4 == 0:
        print(num_list[a_mod][3])
        continue
    else:
        print(num_list[a_mod][b % 4 - 1])



