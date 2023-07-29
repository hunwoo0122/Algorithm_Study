a = int(input())
b = int(input())
c = int(input())
if a+b+c==180:
    if a==b and b==c and a==c:
        print('Equilateral')
    elif (a==b and b!=c) or (b==c and c!=a) or (a==c and a!=b):
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error') 