import sys
input = sys.stdin.readline

row, col = map(int, input().split()) # row 가로=행 , col 세로=열
num = int(input()) # 상점의 개수
store = [] # 1 = 북, 2 = 남, 3 = 서, 4 = 동
for _ in range(num):
    store.append(list(map(int, input().split())))  # 상점의 위치 store 리스트에 삽입
dongeun = list(map(int, input().split())) # 동근의 위치
distance = 0 # 거리의 합 초기화

if dongeun[0] == 1: # 동근의 위치가 북쪽일때
    for i in range(num):
        if store[i][0] == 1: # 상점의 위치가 북쪽일때
            distance += abs(dongeun[1] - store[i][1])
        elif store[i][0] == 2: # 상점의 위치가 남쪽일때
            distance += col
            min_dis = min(store[i][1]+dongeun[1], 2*row-store[i][1]-dongeun[1])
            distance += min_dis
        elif store[i][0] == 3: # 상점의 위치가 서쪽일때
            distance += store[i][1]
            distance += dongeun[1]
        else: # 상점의 위치가 동쪽일때
            distance += (row - dongeun[1])
            distance += store[i][1]      # 위쪽의 경계로부터 거리를 재는 것이므로
elif dongeun[0] == 2: # 동근의 위치가 남쪽일때
    for j in range(num):
        if store[j][0] == 1:
            distance += col
            distance += min(store[j][1]+dongeun[1], 2*row-store[j][1]-dongeun[1])
        elif store[j][0] == 2:
            distance += abs(dongeun[1] - store[j][1])
        elif store[j][0] == 3:
            distance += (col-store[j][1])
            distance += dongeun[1]
        else:
            distance += (col-store[j][1])
            distance += (row-dongeun[1])
elif dongeun[0] == 3: # 동근의 위치가 서쪽일때
    for k in range(num):
        if store[k][0] == 1:
            distance += dongeun[1]
            distance += store[k][1]
        elif store[k][0] == 2:
            distance += (col - dongeun[1])
            distance += store[k][1]
        elif store[k][0] == 3:
            distance += abs(dongeun[1] - store[k][1])
        else:
            distance += row
            distance += min(store[k][1] + dongeun[1], 2*col-store[k][1]-dongeun[1])
else:
    for q in range(num):
        if store[q][0] == 1:
            distance += dongeun[1]
            distance += (row - store[q][1])
        elif store[q][0] == 2:
            distance += (col - dongeun[1])
            distance += (row - store[q][1])
        elif store[q][0] == 3:
            distance += row
            distance += min(store[q][1] + dongeun[1], 2*col-store[q][1]-dongeun[1])
        else:
            distance += abs(dongeun[1] - store[q][1])

print(distance)