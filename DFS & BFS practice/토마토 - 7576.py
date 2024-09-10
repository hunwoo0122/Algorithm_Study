import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
m, n = map(int, input().split()) # m은 상자의 가로 칸의 수, n은 상자의 세로 칸의 수
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
def bfs(result):
    q = deque(result)
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and box[nx][ny] == 0:
                box[nx][ny] = box[a][b] + 1
                q.append((nx, ny))

box = [] # 토마토가 들어있는 상자
for _ in range(n):
    box.append(list(map(int, input().split())))
temp = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            temp.append((i, j))
bfs(temp)

res = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)
# 출력은 토마토가 모두 익을 때까지의 최소 날짜 출력 토마토가 모두 익지 못하면 -1