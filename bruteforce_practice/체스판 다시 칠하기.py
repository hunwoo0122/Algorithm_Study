def count_repainting(board, chess):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != chess[i][j]:
                count += 1
    return count


def main():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        row = input()
        board.append(row)

    min_repaint = float('inf')  # 초기값을 무한대로 설정

    for i in range(N - 7):
        for j in range(M - 7):
            # (i, j)부터 8x8 크기의 체스판 생성
            chess1 = [board[x][j:j + 8] for x in range(i, i + 8)]
            chess2 = [board[x][j:j + 8] for x in range(i, i + 8)]

            # 맨 왼쪽 위 칸이 흰색인 경우와 검은색인 경우에 대해 칠해야 하는 정사각형 개수를 계산하고 최솟값 갱신
            repaint1 = count_repainting(chess1, ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
                                                 "WBWBWBWB", "BWBWBWBW"])
            repaint2 = count_repainting(chess2, ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
                                                 "BWBWBWBW", "WBWBWBWB"])

            min_repaint = min(min_repaint, repaint1, repaint2)

    print(min_repaint)


if __name__ == "__main__":
    main()
