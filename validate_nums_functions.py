def validate_num_sys():
    num_s = input()
    while not num_s.isdecimal():
        num_s = input("Invalid data entered. Enter again ")
    while int(num_s) != 2 and int(num_s) != 10 and int(num_s) != 8 and int(num_s) != 16:
        num_s = input("Invalid data entered. Enter again ")
    num_s = int(num_s)
    if num_s == 2:
        return "bin"
    if num_s == 8:
        return "oct"
    if num_s == 10:
        return "dec"
    if num_s == 16:
        return "hex"


def validate_num_sys_from(num_sys):
    nums_bin = '01'
    nums_oct = '01234567'
    nums_dec = '0123456789'
    nums_hex = '0123456789ABCDEF'
    what_system = []
    if num_sys == "bin":
        what_system = nums_bin
    elif num_sys == "oct":
        what_system = nums_oct
    elif num_sys == "dec":
        what_system = nums_dec
    elif num_sys == "hex":
        what_system = nums_hex
    num = 0
    flag = True
    while flag:
        num = input(f"Enter a number in the {num_sys} number system: ")
        flag = False
        for i in num:
            if i not in what_system:
                print('Invalid data entered. Enter again ')
                flag = True
                break
    return num
