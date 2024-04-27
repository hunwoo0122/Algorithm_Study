import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    array = []
    point = []
    result = 0
    array_2 = []
    cnt = 0
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    student_dict = {}
    for j in range(n):
        array.append(list(map(int, input().split())))
    # 찾으려는 학생의 총점 student로 저장
    student = array[k-1][0] * (35/100) + array[k-1][1] * (45/100) + array[k-1][2] * (20/100)
    for q in range(n):
        point.append(array[q][0] * (35/100) + array[q][1] * (45/100) + array[q][2] * (20/100))
    point.sort(reverse=True) # 오름차순 정렬 총점 성적
    for m in range(n):
        tmp = 0
        cnt += 1
        if cnt <= n//10:
            tmp += 0
        elif cnt <= 2 * (n//10):
            tmp += 1
        elif cnt <= 3 * (n//10):
            tmp += 2
        elif cnt <= 4 * (n//10):
            tmp += 3
        elif cnt <= 5 * (n//10):
            tmp += 4
        elif cnt <= 6 * (n//10):
            tmp += 5
        elif cnt <= 7 * (n//10):
            tmp += 6
        elif cnt <= 8 * (n//10):
            tmp += 7
        elif cnt <= 9 * (n//10):
            tmp += 8
        else:
            tmp += 9
        student_dict[point[m]] = grade[tmp] # len(point)가 10개라고 가정

    print("#{}".format(i), student_dict[student], end=" ")
    print()