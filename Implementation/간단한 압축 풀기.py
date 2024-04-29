t = int(input())

for i in range(1, t + 1):
    n = int(input())
    paper = []
    for j in range(n):
        paper.append(list(input().split()))
        paper[j][1] = int(paper[j][1])
    void = ''
    for k in range(n):
        void += paper[k][0] * paper[k][1]
    print("#{}".format(i), end='')
    for m in range(len(void)):
        if m % 10 == 0:
            print()
        print(void[m], end='')
    print()