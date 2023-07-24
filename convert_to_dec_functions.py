from functions_for_num import *


def bin_oct_to_dec(num, num_sys):
    num = fix_oct_bin_num(num)
    num_sys = 2 if num_sys == "bin" else 8
    num_dec = 0
    if num_sys == 2 or num_sys == 8:
        for i in range(len(num)):
            num_dec += num_sys**i * int(num[i])
    else:
        print("ERROR: function bin_oct_to_dec")
        return 0
    return num_dec


def hex_to_dec(num):
    num = fix_hex_num(num)
    num_dec = 0
    for i in range(len(num)):
        num_dec += 16**i * int(num[i])
    return num_dec
