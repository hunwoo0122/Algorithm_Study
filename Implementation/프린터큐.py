import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    imp = deque(map(int, input().split()))
    imp = deque([(i, idx) for idx, i in enumerate(imp)])
    cnt = 0
    while True:
        if imp[0][0] == max(imp, key=lambda x: x[0])[0]:  # 큐 안에서 중요도가 가장 큰 요소를 찾는데, 이때의 중요도 값을 비교(가장 뒤에 있는 [0])
            cnt += 1
            if imp[0][1] == b:
                print(cnt)
                break
            else:
                imp.popleft()
        else:
            imp.append(imp.popleft())