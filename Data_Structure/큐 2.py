from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    commend = sys.stdin.readline().split()
    if commend[0] == 'push':
        queue.append(int(commend[1]))
    elif commend[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif commend[0] == 'size':
        print(len(queue))
    elif commend[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif commend[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif commend[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])