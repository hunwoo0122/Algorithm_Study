# 맵의 크기 입력
a, b = map(int, input().split())
d = [[0] * b for _ in range(a)] # 리스트 컴프리헨션으로 2차원 리스트 초기화 b는 리스트의 요소 a번만큼 [0]으로 만든다.
# ex) for _ in range(1, a+1):
       # array.append(b)
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(a):
    array.append(list(map(int, input().split())))   # 맵의 정보 입력 0은 육지 1은 바다
#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def turn_left():
    global direction
    direction -=1 # 반시계방향으로 돌아가니까 디렉션이 1만큼 감소
    if direction == -1:
        direction = 3
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0: # d[nx][ny] == 0 이면 가보지 않은 곳 array[nx][ny]이면 육지
        d[nx][ny]=1
        x= nx
        y= ny
        count +=1
        turn_time = 0
        continue # ??
    else:     # 가봤던곳이나 바다이면
        turn_time +=1
    # 네 네방향 모두 갈수 없는경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction] # 뒤로 이동
        if array[nx][ny] == 0: # 뒤로 이동하는곳이 육지이거나 갈수 있으면
            x = nx
            y = ny            # 그방향으로 이동
        else:                 # 뒤로 이동하는 곳이 바다이거나 갈수없으면
            break           # while true 종료 테스트 끝
        turn_time = 0        # 도는 횟수 초기화
print(count)           # 방문한 횟수 출력
