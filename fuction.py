numbers = set(range(1, 10001))
remove_set = set()
for num in numbers:
    for n in str(num):
        num +=int(n)
    remove_set.add(num)
self_number=numbers-remove_set   # 파이썬에서 차집합을쓰면
for i in sorted(self_number):
    print(i)
