croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()
for i in croatia:
    data = data.replace(i, '*')
print(len(data))