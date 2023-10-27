A, B = map(int, input().split())
C, D = map(int, input().split())
def gcd(a,b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

n = gcd(A*D + B*C, B*D)
print(int((A*D + B*C)/n), int(B*D/n))