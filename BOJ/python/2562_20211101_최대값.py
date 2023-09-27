num_list = []
for _ in range(9):
    num_list.append(int(input()))

max = num_list[0]

for n in num_list:
    if n > max:
        max = n

print(max)
print(num_list.index(max)+1)
