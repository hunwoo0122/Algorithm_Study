# 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    cnt = 0
    array = []
    a = int(sys.stdin.readline())
    for i in range(3, a):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            array.append(i)

    start , end = 0, len(array)-1

    while array[start] <= array[end]:
        if array[start] + array[end] == a:
            cnt += 1
            start += 1
            end -= 1
        elif array[start] + array[end] < a: # 두 요소의 합이 a보다 작을때 제일 작은 요소인 start인덱스의 요소를 다음 인덱스로 추가
            start += 1
        else:
            end -= 1
    print(cnt)