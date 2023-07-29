h, w = map(int, input().split())  # h=세로, w=가로               # n=막대의 개수
# l = 막대의 길이 d=방향(1=세로 0=가로) 좌표(x,y)

location=[]
for i in range(h):
    location.append([])
    for j in range(w):
        location[i].append(0)
# w x h 크기의 판완성
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split()) # 막대의 길이, 방향, 시작좌표
    if d == 0:  # 막대가 가로이면
        for j in range(l):
            location[x-1][y+j-1] = 1
    else:
        for k in range(l):
            location[x+k-1][y-1] = 1

for i in range(h):
    for j in range(w):
        print(location[i][j], end=' ')
    print()