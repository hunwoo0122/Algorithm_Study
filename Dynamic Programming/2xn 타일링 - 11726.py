import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
    sys.exit(0)
dp = [0 for i in range(n)]
dp[0], dp[1] = 1, 2
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1] % 10007)