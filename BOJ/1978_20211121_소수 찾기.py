def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for k in range(2, num): # 2부터 자기자신보다 1작은 수로 나누어떨어지면 소수 X
            if num % k == 0:
                return False
        return True

N = int(input())
num_list = list(map(int, input().split()))
count = 0

for num in num_list:
    if isPrime(num):
        count += 1
             
print(count)
        
