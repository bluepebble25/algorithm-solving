word = input()
orgin = []
for w in word:
    ascii_num = ord(w)
    if ascii_num >= 68:
        orgin.append(chr(ascii_num-3))
    else:
        orgin.append(chr(ascii_num + 23))
print(''.join(orgin))
