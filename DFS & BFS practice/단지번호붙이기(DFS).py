import sys
input = sys.stdin.readline

n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        graph[x][y] = 0
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

result = 0
count = 0
cnt = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            cnt.append(count)
            result += 1
            count = 0

print(result)
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])