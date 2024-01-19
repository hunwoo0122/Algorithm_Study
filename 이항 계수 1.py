n, k = map(int, input().split())
m = 1
r = 1
o = 1
for i in range(1,n+1):
    m = m * i
for j in range(1,k+1):
    r = r * j
for k in range(1,n-k+1):
    o = o * k
print(m // (o*r))