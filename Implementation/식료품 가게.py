import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    ob = list(map(int, input().split()))
    array = []
    while ob:
        for j in range(len(ob)):
            if ob[j] % 4 == 0 and int(ob[j] * (3/4)) in ob: # 정상가가 리스트에 있는지 검사
                a = ob.pop(j)        # 리스트를 pop할때는 인덱스로 pop함
                idx = ob.index(int(a * (3/4)))
                b = ob.pop(idx)
                array.append(b)
                break


    print("#{}".format(i), *array, end=" ")
    print()