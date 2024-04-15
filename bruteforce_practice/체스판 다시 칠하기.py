import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
INF = 21470000000
min_repainting = INF
def cut_repainting(board, chess):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != chess[i][j]:
                cnt += 1
    return cnt

for _ in range(n):
    board.append(list(input().strip()))

for i in range(n-7):
    for j in range(m-7):
        temp_chess1 = [board[x][j:j+8] for x in range(i, i+8)]
        temp_chess2 = [board[x][j:j+8] for x in range(i, i+8)]

        repaint1 = cut_repainting(temp_chess1, ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
                                                'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
                                                'WBWBWBWB', 'BWBWBWBW'])
        repaint2 = cut_repainting(temp_chess2, ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW',
                                                'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
                                                'BWBWBWBW', 'WBWBWBWB'])
        min_repainting = min(min_repainting, repaint1, repaint2)

print(min_repainting)