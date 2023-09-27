num = int(input())
num_list = []

num_list = list(map(int, input().split()))

if len(num_list) == 1:
    print(num_list[0] * num_list[0])
else:
    print(min(num_list) * max(num_list))
