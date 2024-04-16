import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().strip())))
def bfs(graph, a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                count += 1
                q.append((nx, ny))
    return count
cnt = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            cnt.append(bfs(array, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
