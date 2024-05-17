t = int(input())

for i in range(1, t + 1):
    p, q = map(int, input().split())
    p_sum = 0
    px = 0
    py = 0
    pDiagonal = 1        # 몇 번째 대각선인지 체크
    while True:
        p_sum += pDiagonal  # p_sum은 해당 대각선에서 최댓값
        if p_sum >= p:
            px = pDiagonal - (p_sum - p)
            py = (pDiagonal + 1) - px
            break
        pDiagonal += 1

    q_sum = 0
    qx = 0
    qy = 0
    qDiagonal = 1
    while True:
        q_sum += qDiagonal
        if q_sum >= q:
            qx = qDiagonal - (q_sum - q)
            qy = (qDiagonal + 1) - qx
            break
        qDiagonal += 1

    newX = px + qx
    newY = py + qy
    newSum = 0
    newDiagonal = newX + newY - 1

    for j in range(1, newDiagonal + 1): # newSum은 합쳐진 좌표의 값
        newSum += j                # 일단 해당 대각선의 최댓값 구함
    newSum -= (newDiagonal - newX)  #
    print("#{}".format(i), newSum, end=" ")
    print()