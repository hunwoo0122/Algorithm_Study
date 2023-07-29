x = int(input())

line = 0
max_num=0
while x > max_num:
    line += 1 # 라인을 1씩증가시켜서 입력한 순서의 라인을 알아낸다
    max_num += line

gap = max_num - x
if line % 2 == 0:
    top = line - gap # top 분자
    down = gap + 1  # down 분모
else:
    top = gap + 1 # 내림차순
    down = line - gap