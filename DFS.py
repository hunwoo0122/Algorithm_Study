X =int(input())
N = int(input())
m=[]
for i in range(N):
    a,b=map(int, input().split())
    k = a*b
    m.append(k)
x=sum(m)
if x==X:
    print("Yes")
else:
    print("No")

