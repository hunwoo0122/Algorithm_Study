import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    sosu = []
    for i in range(2, n): # 2부터 입력된 범위 n-1까지 탐색
        error = 0
        for j in range(2, i): # 2~n-1까지 소수인지 판별
            if i % j == 0:  # 만약 i가 소수이면 error 1증가
                error += 1
        if error == 0:   # i가 소수이면
            sosu.append(i)
    partition = []
    for k in range(len(sosu)):
        for q in range(k, len(sosu)):
            if sosu[k] + sosu[q] == n:
                partition.append([sosu[k], sosu[q]]) # 골드바흐 파티션의 2차원 리스트 생성

    min_diff = abs(partition[0][0]-partition[0][1])
    min_pair = partition[0]

    for pair in partition:
        diff = abs(pair[0] - pair[1])
        if diff < min_diff:
            min_diff = diff
            min_pair = pair
    print(*min_pair)

