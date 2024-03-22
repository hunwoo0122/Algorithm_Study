import sys
input = sys.stdin.readline
n, m = map(int, input().split())

visited = [False] * (n + 1)
result = []

def backtrack(cnt):
    if cnt == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack(cnt + 1)
            visited[i] = False
            result.pop()
        else:
            result.append(i)
            backtrack(cnt + 1)
            visited[i] = False
            result.pop()


backtrack(0)
# N과 M(1)에서 중복 허용