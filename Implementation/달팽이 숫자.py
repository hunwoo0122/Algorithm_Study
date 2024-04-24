import sys
sys.stdin = open("input.txt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    x, y = 0, 0          # 방향전환에 필요한 초기값
    dist = 0              # 방향에 필요한 인자
    array = [[0] * N for _ in range(N)]    # 초기 배열
    for j in range(1, N*N + 1):
        array[x][y] = j
        x = x + dx[dist]
        y = y + dy[dist]
        if x < 0 or y < 0 or x >= N or y >= N or array[x][y] != 0: # 달팽이가 판의 범위를 넘거나 이미 지나친 경우
            x = x - dx[dist]
            y = y - dy[dist] # 실행 취소

            dist = (dist + 1) % 4 # 사이클 실행

            x = x + dx[dist]
            y = y + dy[dist] # 다시 실행

    print("#{}".format(i))

    for row in array:
        print(*row)