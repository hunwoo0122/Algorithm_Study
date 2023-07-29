d = []
for i in range(10):
    d.append(list(map(int, input().split())))

# 먹이를 찾았을때와 맨 아래의 가장 오른쪽에 도착한 경우 더 이상 움직일 수없는 경우
# 고려
x,y=1,1        # 개미의 시작좌표
while True:
    if d[x][y]==0:      # 개미가 갈수있는 곳이면 go
        d[x][y]=9
    elif d[x][y]==2:   # 먹이를 찾으면 break
        d[x][y]=9
        break

    if d[x+1][y]==1 and d[x][y+1]==1:       # 오른쪽 아래쪽이 벽으로 막혀있으면 break
        break

    if d[x][y+1] == 1:          # 오른쪽으로 가다가 오른쪽이 막혀있으면 아래쪽으로 이동
        x = x+1
    else:                       # 오른쪽이 갈수있으면 오른쪽이동
        y = y+1

for i in range(10):
    for j in range(10):
        print(d[i][j], end=' ')
    print()
