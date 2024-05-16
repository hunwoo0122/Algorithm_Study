def is_palindrome(s):
    return s == s[::-1]

def find_max_palindrome_length(board):
    max_len = 1

    # 행(row) 검사
    for length in range(100, max_len, -1):
        for start in range(101 - length):
            substring = board[start:start + length]
            if is_palindrome(substring):
                max_len = length
                break
        if max_len == length:
            break
    line = [[board[j][i] for j in range(100)] for i in range(100)]
    # 열(column) 검사
    for length in range(100, max_len, -1):
        for start in range(101 - length):
            substring = line[start:start + length]
            if is_palindrome(substring):
                max_len = length
                break
        if max_len == length:
            break

    return max_len

for _ in range(1, 11):  # 10개 테스트 케이스
    test = int(input())
    board = []
    for j in range(100):
        board.append(list(input()))

    max_palindrome_length = find_max_palindrome_length(board)
    print("#{}".format(test), max_palindrome_length, end=" ")

