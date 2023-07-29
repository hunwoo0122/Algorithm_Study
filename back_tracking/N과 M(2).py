def backtracking(result, used, n, m):
    if len(result) == m:  # 길이가 m인 수열이 생성된 경우
        if result == sorted(result):  # 수열이 오름차순인 경우에만 출력
            print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            result.append(i)
            backtracking(result, used, n, m)
            used[i] = False
            result.pop()


n, m = map(int, input().split())
result = []
used = [False] * (n + 1)
backtracking(result, used, n, m)
