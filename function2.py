array = list(range(1, 10001))
remove_list = []
for number in array:
    for num in str(number):
        number += int(num)
    if number <= 10000:            # 생성자는 10000이하이여야 하므로
        remove_list.append(number)
for remove_num in set(remove_list):
    array.remove(remove_num)
for self_number in array:
    print(self_number)
