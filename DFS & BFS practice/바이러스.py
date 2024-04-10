import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]
cnt = 0
array = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    array.append(v)
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]:
            dfs(i)
    return len(array)
print(dfs(1)-1)