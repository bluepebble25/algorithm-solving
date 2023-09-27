N = int(input())
name_list = []
result = ""
flag = False
for _ in range(N):
    name_list.append(input())

if N == 1:
    print(name_list[0])
else:
    for k in range(len(name_list[0])):
        for i in range(N):
            if name_list[0][k] == name_list[i][k]:
                flag = True
            else:
                flag = False
                result += "?"
                break
                
        if flag == True:
            result += name_list[0][k]
            flag = False

    print(result)
