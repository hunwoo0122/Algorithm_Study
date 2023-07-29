dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
data = input()
cnt = 0
for i in range(len(data)):
    for j in dial:
        if data[i] in j:
            cnt +=dial.index(j)+3
print(cnt)
