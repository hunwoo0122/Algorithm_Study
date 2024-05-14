import sys
input = sys.stdin.readline

def dfs(idx, flavor, kal):
    global maxTaste

    # 총 칼로리를 넘으면 리턴
    if kal > l:
        return

    # taste의 합이 제일큰 tate 합보다 크면 갱신
    if maxTaste < flavor:
        maxTaste = flavor

    if idx == n:
        return
    f, k = food[idx]

    # 햄버거 재료 리스트에서 재료를 사용했을 때
    dfs(idx + 1, flavor + f, kal + k)
    # 햄버거 재료 리스트에서 재료를 사용하지 않았을 때
    dfs(idx + 1, flavor, kal)


t = int(input())
for i in range(1, t + 1):
    n, l = map(int, input().split())
    food = []
    for j in range(n):
        food.append(list(map(int, input().split())))
    maxTaste = 0
    dfs(0, 0, 0)

    print("#{}".format(i), maxTaste, end=" ")
    print()