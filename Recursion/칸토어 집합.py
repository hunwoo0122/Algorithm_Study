import sys
input = sys.stdin.readline
# a는 시작점 n은 끝점
def cut(a, n): # a = 시작점
    if n == 1:
        return
    for i in range(a + n//3, a +(n//3)*2): # 가운데 문자열을 공백으로
        result[i] = ' '
    cut(a, n//3)
    cut(a + n//3 * 2, n//3)

while True:
    try:
        N = int(input())
        result = ['-']*(3**N)
        cut(0, 3**N)
        print(''.join(result))
    except : # EOF 발생시
        break # 종료