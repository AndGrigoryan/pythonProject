def remove_leading_zeros(num):
    i = 0
    while i < len(num):
        if num[0] == "0":
            num = num[i + 1:]
        else:
            i += 1
    return num


def fix_oct_bin_num(num):
    num = remove_leading_zeros(num)
    return num[::-1]


def fix_hex_num(num):
    num = remove_leading_zeros(num)
    num = num[::-1]
    tmp = []
    for i in num:
        if i.isdecimal():
            tmp.append(i)
        else:
            tmp.append(ord(i) - 55)
    return tmp


def fix_dec_to_hex_num(num):
    fix_hex = []
    for i in range(len(num)-1, -1, -1):
        if num[i] > 9:
            fix_hex.append(chr(int(num[i]) + 55))
        else:
            fix_hex.append(num[i])
    return fix_hex
