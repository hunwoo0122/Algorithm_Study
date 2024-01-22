import sys
input = sys.stdin.readline
n = int(input())
dancer = {'ChongChong'}
for _ in range(n):
    human, meeting = input().strip().split()
    if human in dancer:
        dancer.add(meeting)

    if meeting in dancer:
        dancer.add(human)
print(len(dancer))