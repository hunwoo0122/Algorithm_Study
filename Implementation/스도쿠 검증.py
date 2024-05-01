import sys
input = sys.stdin.readline

t = int(input())
# 스도쿠에서 겹치는 숫자가 없을 경우 1, 그렇지 않을 경우 0 출력
def sudoku_checking(sudoku):
    for i in range(9):
        col_num = [0] * 10
        row_num = [0] * 10
        for j in range(9):
            col = sudoku[i][j]
            row = sudoku[j][i]
            if col_num[col]: return 0
            if row_num[row]: return 0
            col_num[col] = 1
            row_num[row] = 1

            if i % 3 == 0 and j % 3 == 0:
                square_num = [0] * 10
                for k in range(i, i + 3):
                    for m in range(j, j + 3):
                        square = sudoku[k][m]
                        if square_num[square]: return 0
                        square_num[square] = 1
    return 1

for i in range(1, t+1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    print("#{}".format(i), sudoku_checking(sudoku), end=" ")
    print()