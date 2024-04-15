import sys
input = sys.stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= M:
        start = mid + 1
    else:
        end = mid - 1 # while문의 마지막인 start > end가 되는 과정에서
        # end가 mid -1 이 되므로 M의 최소값이 출력됨 그래서 end를 출력해야함
print(end)