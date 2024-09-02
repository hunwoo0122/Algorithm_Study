import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(dist[v])
            break
        for nx in (v + 1, v - 1, 2*v):
            if (0<= nx <=MAX) and not dist[nx]: # 여기서 왜 not dist[nx]를 설정하냐면 시간이 아직 기록되지 않았기 때문
                dist[nx] = dist[v] + 1
                q.append(nx)

MAX = 10**5
dist = [0] * (MAX + 1) # dist의 값은 시간, dist의 인덱스는 수빈이의 위치
n, k = map(int, input().split())
bfs()