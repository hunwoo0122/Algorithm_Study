import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def DFS(array, x, y, visited):
    if x < 0 or x >= len(array) or y < 0 or y >= len(array[0]):
        return
    if visited[x][y] or array[x][y] == 0:
        return

    visited[x][y] = True

    DFS(array, x + 1, y, visited)
    DFS(array, x - 1, y, visited)
    DFS(array, x, y + 1, visited)
    DFS(array, x, y - 1, visited)

for i in range(T):
    cnt = 0
    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for j in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1
    for k in range(len(field)):
        for q in range(len(field[0])):
            if field[k][q] == 1 and not visited[k][q]:
                DFS(field, k, q, visited)
                cnt += 1
    print(cnt)