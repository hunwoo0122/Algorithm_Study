n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i)
            visited[i] = False
            s.pop()


dfs(1)