def count_subsets_dp(arr, target_sum):
    n = len(arr)
    dp = [0] * (target_sum + 1)
    dp[0] = 1

    for num in arr:
        for j in range(target_sum, num - 1, -1): # 리스트안의 num일때 구하려는 k와 num사이의 j가 될수 있는 경우의 수를 모두 구한다
            dp[j] += dp[j - num] # num일때 j-num의 경우의수는 곧 j의 경우의 수가 된다. num을 더하기만 하면 되니까

    return dp[target_sum]

# 테스트 케이스 수 입력
T = int(input())

for case in range(1, T + 1):
    # 수열의 길이 N과 목표 합 K 입력
    N, K = map(int, input().split())

    # 수열 입력
    sequence = list(map(int, input().split()))

    # 부분집합의 합이 K가 되는 경우의 수 계산
    result = count_subsets_dp(sequence, K)

    # 결과 출력
    print("#{} {}".format(case, result))