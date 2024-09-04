import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n = int(input())
ground = []
def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx <n) and (0<= ny <n) and not visited[nx][ny] and ground[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx, ny, h)

for _ in range(n):
    ground.append(list(map(int, input().split())))

ans = 1
for i in range(max(map(max, ground))):
    visited = [[False] * n for _ in range(n)]
    size = 0
    for j in range(n):
        for k in range(n):
            if ground[j][k] > i and not visited[j][k]:
                size += 1
                dfs(j, k, i)
    ans = max(ans, size)

print(ans)