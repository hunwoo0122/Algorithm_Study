import sys
input = sys.stdin.readline

n = int(input())

stairs = [0 for _ in range(301)]
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열 초기화
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식 계산
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    # 바텀업과정에서 max함수를 통해 동적으로 dp배열에 각 계단마다 알맞은 최댓값이 배정된다.

print(dp[n])