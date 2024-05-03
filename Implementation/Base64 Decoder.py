import sys
sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t + 1):
    sentence = input()
    length = len(sentence)
    decode=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '+', '/']
    res = ''
    for alphabet in sentence:
        value = decode.index(alphabet)
        bin_num = str(bin(value)[2:])

        while len(bin_num) < 6:
            bin_num = '0' + bin_num

        res += bin_num     #
    r = ''
    for j in range(length * 6 // 8):
        e = int(res[j*8 : j*8+8], 2)
        r += chr(e)
    print("#{}".format(i), r, end=" ")
    print()