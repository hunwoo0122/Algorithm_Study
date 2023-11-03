while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1, 2*n+1): # n보다 크고 2n보다 작거나 같은 i의 수중에 소수가 있는지 탐색
        is_prime = True
        for j in range(2, int(i**0.5)+1):   # i의 소수 판별
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            cnt += 1
    print(cnt)

