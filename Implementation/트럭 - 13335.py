import sys
from collections import deque
input = sys.stdin.readline

# 트럭의 수, 다리의 길이, 다리의 최대 하중
n, w, L = map(int, input().split())
truck = list(map(int, input().split())) # 트럭의 수
bridge = deque()
time = 0
idx = 0
for _ in range(w):
    bridge.append(0)  # 다리에 가중치를 세워줌

while idx < n: # 트럭의 인덱스 n일때 멈춤
    time += 1
    bridge.popleft()
    if sum(bridge)+truck[idx] <= L: #
        bridge.append(truck[idx])
        idx += 1
    else:
        bridge.append(0)
while bridge:       # 마지막 트럭이 다 지나갈때까지 시간체크
    time += 1
    bridge.popleft()

print(time)