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
            if (0<= nx <=MAX) and not dist[nx]: # 여기서 왜 not dist[nx]를 설정하냐면 dist[nx]가 0이 아니라는 건 전에 방문했다는
                # 뜻이고  for문과 큐를 이용해 반복문을 돌려본결과 k에 도달하지 않는다는 것이기 때문에 굳이 한번 더 dist[nx]로
                # 갈 필요가 없기 때문에 시간복잡도와 메모리용량을 줄일 수 있음 dist[nx] != 0 인 경우는
                # 진작부터 탐색하기 때문(중복 탐색을 피하기 위해)
                dist[nx] = dist[v] + 1
                q.append(nx)

MAX = 10**5
dist = [0] * (MAX + 1) # dist의 값은 시간, dist의 인덱스는 수빈이의 위치
n, k = map(int, input().split())
bfs()