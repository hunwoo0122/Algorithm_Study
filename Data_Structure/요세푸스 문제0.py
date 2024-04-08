import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
queue = deque()
answer = []
n = 1
for _ in range(a):
    queue.append(n)
    n += 1
while len(answer) != a:
    for _ in range(b-1):
        queue.append(queue.popleft())  # b-1번째 만큼 popleft해주고
    answer.append(queue.popleft()) # b번째 popleft
formatted_output = "<" + ", ".join(map(str, answer)) + ">"
print(formatted_output)