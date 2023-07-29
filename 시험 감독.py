n = int(input())
teaster = list(map(int, input().split()))
a, b = map(int, input().split())

cnt = n    # 총감독관의 최소 수
for i in teaster:
    i -= a            # 각 시험장에 있는 응시자들중 총감독관이 감시할수 있는 인원은 뺌(각 시험장에 총감독관은 꼭 1명 있어야하므로)
    if i > 0:           # 부감독관이 감시할수있는 인원이 있을 경우
        if i % b == 0:
            cnt += (i//b)
        else:
            cnt += (i//b) + 1 # 만약 딱 나눠떨어지지않고

print(cnt)