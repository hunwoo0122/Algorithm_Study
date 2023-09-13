import sys
import math

a, b = map(int, sys.stdin.readline().split())

# 최대공약수(GCD) 계산
gcd = math.gcd(a, b)

# 최소공배수(LCM) 계산
lcm = (a * b) // gcd

print(lcm)
