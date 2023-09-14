import sys

a, b =map(int, sys.stdin.readline().split())
a_Array = set((map(int, sys.stdin.readline().split())))
b_Array = set((map(int, sys.stdin.readline().split())))

print(len(a_Array-b_Array)+len(b_Array-a_Array))


