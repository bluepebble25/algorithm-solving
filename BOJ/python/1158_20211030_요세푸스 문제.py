N, K = map(int, input().split())
arr = [i for i in range(1,N+1)]
result = []
index = 0

while len(arr)>0:
    index += K-1
    index %= len(arr)
    result.append(arr[index])
    del arr[index]

print("<",end='')
print(", ".join(map(str, result)), end='')
print(">")