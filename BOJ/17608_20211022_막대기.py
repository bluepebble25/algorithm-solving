import sys

n = int(input())
stick_arr = []
for _ in range(n):
    stick_arr.append(int(sys.stdin.readline()))

count = 1
temp = stick_arr[n-1]
for i in range(n-2,-1,-1):
    if temp < stick_arr[i]:
        temp = stick_arr[i]
        count += 1

print(count)


