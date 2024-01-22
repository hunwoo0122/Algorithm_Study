import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
array = set()
for _ in range(n):
    chat = input().strip()
    if chat != 'ENTER':
        array.add(chat)
    else:
        cnt += len(array)
        array.clear()
cnt += len(array)
print(cnt)