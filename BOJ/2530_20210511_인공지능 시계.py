a,b,c = map(int, input().split(' '))
t = a * 3600 + b * 60 + c
d = int(input())
t += d

if (t >= 86400) & (t % 86400 == 0): #하루보다 시간이 길고 나머지가 0이면 0시 0분 0초
    a, b, c = 0, 0, 0
else:
    if t > 86400: #하루보다 시간이 길 때
        t = t - int(t / 86400) * 86400 #일을 뺀 시, 분, 초 남김
        
    a = int(t / 3600) #시간 -> 3600으로 나눈 몫
    t = t - a * 3600
    b = int(t / 60) #분 -> 시간만 남은 t를 60으로 나눈 몫
    t = t - b * 60
    c = t

print(a,b,c)
