for tc in range(1, int(input())+1):
    data, k = input().split()
    k = int(k)
    n = len(data)
    now = set([data])
    nxt = set()
    for _ in range(k):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(n):
                for j in range(i+1, n):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    print('#{}'.format(tc), max(map(int, now)), end=" ")
    print()