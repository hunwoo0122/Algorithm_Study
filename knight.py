input_data=input()
row = int(input_data[1])
col = int(ord(input_data[0]))-int(ord('a'))+1 # 유니코드로 문자 'a'는 97 'z'는 122

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
count = 0
for step in steps:
    next_row = row + step[0]         # step[0]는 steps의 x축
    next_col = col + step[1]
    if next_row <= 8 and next_col <= 8 and next_row >= 1 and next_col >= 1:
        count +=1
print(count)