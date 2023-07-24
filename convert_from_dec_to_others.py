from functions_for_num import *


def dec_to_bin(num):
    num_bin = []
    num = int(num)
    while num != 0:
        num_bin.append(num % 2)
        num //= 2

    return num_bin[::-1]


def dec_to_oct(num):
    num_oct = []
    num = int(num)
    while num != 0:
        num_oct.append(num % 8)
        num //= 8

    return num_oct[::-1]


def dec_to_hex(num):
    num_hex = []
    num = int(num)
    while num != 0:
        num_hex.append(num % 16)
        num //= 16
    num_hex = fix_dec_to_hex_num(num_hex)

    return num_hex
