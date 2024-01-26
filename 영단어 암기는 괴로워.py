import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
for _ in range(n):
	name = input().strip()
	if len(name) < m:
		continue
	if d.get(name): # 만약 현재 문자열이 이미 딕셔너리에 존재한다면 등장 횟수를 1 증가
		d[name][0] += 1
	else: # 그렇지 않으면 딕셔너리에 새로운 항목을 추가하고 등장 횟수를 1, 길이를 현재 문자열의 길이, 문자열 자체를 현재 문자열로 초기화
		d[name] = [1, len(name), name]
# 개수, 길이는 내림차 순으로 단어는 사전순(오름차 순)으로 정렬
ans = sorted(d.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in ans:
	print(a[0])