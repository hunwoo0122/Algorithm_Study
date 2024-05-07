import sys
input = sys.stdin.readline

for i in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    view = 0
    for j in range(2, n-2): # 빌딩의 3번째부터 n-3번째까지
        max_right = 0
        max_left = 0
        max_height = 0
        if max_right < max(building[j-2], building[j-1]):
            max_right = max(building[j-2], building[j-1])
        if max_left < max(building[j+2], building[j+1]):
            max_left = max(building[j+2], building[j+1])
        if max_right > max_left:
            max_height = max_right
        else:
            max_height = max_left
        if building[j] > max_height:
            view += building[j] - max_height
        else:
            view += 0
    print("#{}".format(i), view, end=" ")
    print()