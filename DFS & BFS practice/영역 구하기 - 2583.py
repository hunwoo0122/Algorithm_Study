import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    size = 1
    graph[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and not graph[nx][ny]:
                size += 1
                q.append((nx, ny))
                graph[nx][ny] = 1
    result.append(size)


m, n, k = map(int, input().split()) # m은 세로 n은 가로
graph = [[0] * n for _ in range(m)]  # 직사각형이 없는 곳은 0으로
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1 # 직사각형은 1로
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)
result.sort()
num = len(result)
print(num)
for i in result:
    print(i, end=' ')