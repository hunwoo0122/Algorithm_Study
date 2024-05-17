t = int(input())

dx = [0, 0, 1, 1, -1, -1, 1, -1]
dy = [1, -1, 1, -1, 1, -1, 0, 0]
# 1은 흑돌 2는 백돌 (2, 3)은 x축으로 2 y축으로 3
for i in range(1, t + 1):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2][n // 2] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    for j in range(m):
        x, y, c = map(int, input().split())
        x = x - 1
        y = y - 1
        reverse = []
        for k in range(8):  # 놓은 위치에서 모든 방향 탐색
            nx = x + dx[k]
            ny = y + dy[k]
            while True:
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    reverse = []
                    break
                if board[ny][nx] == 0:
                    reverse = []
                    break
                if board[ny][nx] == c:
                    break
                else:
                    reverse.append((ny, nx))
                nx = nx + dx[k]
                ny = ny + dy[k]
            for ny, nx in reverse:
                if c == 1:
                    board[ny][nx] = 1
                else:
                    board[ny][nx] = 2
        board[y][x] = c

    w, b = 0, 0
    for j in range(n):
        for k in range(n):
            if board[j][k] == 1:
                w += 1
            elif board[j][k] == 2:
                b += 1
    print("#{}".format(i), w, b, end=" ")
    print()