import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def dfs(x, y):
    global cnt
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < b) and (0 <= ny < a) and not visited[nx][ny] and square[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny)

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    visited = [[False] * a for _ in range(b)]
    square = []
    cnt = 0
    for i in range(b):
        square.append(list(map(int, input().split())))
    for i in range(b):
        for j in range(a):
            if square[i][j] == 1 and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j)
    print(cnt)