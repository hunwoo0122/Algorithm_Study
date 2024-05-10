import sys
input = sys.stdin.readline

for i in range(1, 11):
    n = int(input())
    board = []
    cnt = 0
    for j in range(8):
        board.append(input().strip())  # strip() 함수를 이용하여 개행 문자를 제거해줍니다.

    # 가로 방향 회문 검사
    for m in range(8):   # 행 검사
        for k in range(8 - n + 1):  # 범위를 조정하여 인덱스 오류를 방지합니다.(열 검사)
            if board[m][k:k + n] == board[m][k:k + n][::-1]:  # 회문인지 확인합니다.
                cnt += 1

    # 세로 방향 회문 검사
    for m in range(8):
        for k in range(8 - n + 1):  # 범위를 조정하여 인덱스 오류를 방지합니다.
            column = ''.join(board[l][m] for l in range(k, k + n))  # 세로 방향 문자열을 만듭니다.
            if column == column[::-1]:  # 회문인지 확인합니다.
                cnt += 1

    print("#{}".format(i), cnt)
