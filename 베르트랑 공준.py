while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1, 2*n+1): # n보다 크고 2n보다 작거나 같은 i의 수중에 소수가 있는지 탐색
        is_prime = True
        for j in range(2, int(i**0.5)+1):   # i의 소수 판별
            if i % j == 0: # i가 소수가 아닐 경우
                is_prime = False
                break  # for j..문을 종료하고 계속 진행 is_prime은 False인 채로 남음
        if is_prime:  # i가 소수일 경우만
            cnt += 1
    print(cnt)

