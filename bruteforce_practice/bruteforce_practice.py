def BruteForce(p, t):  # t: 원본문자열 p: 찾고자 하는 문자열 패턴
    i = 0 # t의 검색 인덱스
    j = 0 # p의 검색 인덱스
    while i < len(t) and j < len(p): # i < 18, j < 6 찾으려는 패턴을 다 찾았으면 j == len(p) 원본 문자열의 끝에 다다르면 못찾은거?
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i - len(p)  # 찾을 경우 문자열 위치 반환
    else:
        return -1 # 못찾았으면 fail

pattern = "Python" # len(p)는 6
text = "Hello Python World" # len(t)는 18
print(BruteForce(pattern, text))