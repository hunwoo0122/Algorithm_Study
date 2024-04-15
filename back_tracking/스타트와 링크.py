import sys
input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
visited = [False for _ in range(n)]
INF = 21470000000
res = INF
# A와 B는 다른팀
def dfs(L, idx):   # 여기서 idx는 visited리스트의 방문기록을 기록하는데 쓰는 for문의 반복 변수 인덱스
    # L은 방문기록이 N//2 가 되도록 하는 매개체
    global res
    if L == n //2:
        A = 0
        B = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += array[i][j]
                elif not visited[i] and not visited[j]:
                    B += array[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(L+1, i+1)
            visited[i] = False
dfs(0, 0)
print(res)