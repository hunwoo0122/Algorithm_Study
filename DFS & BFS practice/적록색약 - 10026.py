import sys
input = sys.stdin.readline
from collections import deque

# r, g 색약은 r, g를 구분 못함
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]

def bfs(x, y):
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and grid[a][b] == grid[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

for i in range(n):
    grid.append(list(input().strip()))
# 적록 색맹이 아닌 사람의 경우
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1
print(cnt1, end=" ")

visited = [[False] * n for _ in range(n)]

# 적록 색맹인 사람인 경우
cnt2 = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1
print(cnt2)
