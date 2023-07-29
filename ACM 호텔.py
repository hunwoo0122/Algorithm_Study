t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    room = 101
    if n == 1:
        room = 101
    else:
        if n%h ==0:
            share = n//h
            room = h*100 + share
        else:
            for j in range(2, n+1):
                room += 100
                if j % h == 0:
                    room -= 100 * h
                    room += 1
    print(room)