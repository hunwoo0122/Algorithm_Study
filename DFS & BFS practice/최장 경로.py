import sys
input = sys.stdin.readline
# 테스트 케이스 수 입력
t = int(input())
# n은 정점의 개수, m은 간선의 개수
# m개의 줄에 그래프의 간선 정보를 나타내는 두 정수 x, y
def dfs(start, cnt):
    global result
    visited[start] = 1
    for i in node[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, cnt + 1)
    visited[start] = 0
    if cnt > result:
        result = cnt

for tc in range(1, t + 1): # 리스트는 메인함수와 정의되는 함수가 공유됨
    n, m = map(int, input().split())
    node = [[] for i in range(n + 1)]  # 정점의 개수 만큼 빈 노드 선언
    result = 0
    for _ in range(m):
        x, y = map(int, input().split())
        node[x].append(y)
        node[y].append(x)
    for j in range(1, n + 1):  # 시작하는 정점 다 탐색
        visited = [0] * (n + 1)
        dfs(j, 1)
    print("#{}".format(tc), result, end=" ")
    print()