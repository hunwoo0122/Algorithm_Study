import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
ans = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
queue = deque()
queue.append(1)

def bfs():
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if ans[i] == 0:
                ans[i] = v
                queue.append(i)
bfs()
node = ans[2:]
for i in node:
    print(i)