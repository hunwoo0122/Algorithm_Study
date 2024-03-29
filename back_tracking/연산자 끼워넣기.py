import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split())) # 4개의 정수 앞에서부터 덧셈, 뺄셈, 곱셈, 나눗셈 갯수

maximum = -1e9
minimum = 1e9
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
                       # //가 아니라 int(/) 인 이유는 음수일 때 // 는 내림차순이 된다
dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)