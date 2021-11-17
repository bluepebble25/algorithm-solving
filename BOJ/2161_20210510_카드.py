from collections import deque

n = int(input())
mycard = deque([n for n in range(1, n+1)])
discard = []
i = n

while(i>1):
    discard.append(mycard.popleft())
    mycard.append(mycard.popleft())
    i = i - 1

discard.append(mycard.pop())
print(" ".join(map(str, discard)))
