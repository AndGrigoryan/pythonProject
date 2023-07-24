from convert_to_dec_functions import *
from validate_nums_functions import *
from convert_from_dec_to_others import *

print("Conversion calculator")

print("From: ", end="")
num_sys_from = validate_num_sys()

print("To: ", end="")
num_sys_to = validate_num_sys()
while num_sys_to == num_sys_from:
    print("ERROR: Choose a different number system")
    num_sys_to = validate_num_sys()


num = validate_num_sys_from(num_sys_from)

num_dec = 0

if num_sys_to == "dec":
    if num_sys_from == "bin" or num_sys_from == "oct":
        num_dec = bin_oct_to_dec(num, num_sys_from)
    elif num_sys_from == "hex":
        num_dec = hex_to_dec(num)
    print(f"{num_sys_to}: {num_dec}")
elif num_sys_to == "bin":
    if num_sys_from == "oct":
        num_dec = bin_oct_to_dec(num, num_sys_from)
    elif num_sys_from == "hex":
        num_dec = hex_to_dec(num)
    else:
        num_dec = num
    num_bin = dec_to_bin(num_dec)
    print(f"{num_sys_to}: ", *num_bin, sep="")
elif num_sys_to == "oct":
    if num_sys_from == "bin":
        num_dec = bin_oct_to_dec(num, num_sys_from)
    elif num_sys_from == "hex":
        num_dec = hex_to_dec(num)
    else:
        num_dec = num
    num_oct = dec_to_oct(num_dec)
    print(f"{num_sys_to}: ", *num_oct, sep="")
elif num_sys_to == "hex":
    if num_sys_from == "bin" or num_sys_from == "oct":
        num_dec = bin_oct_to_dec(num, num_sys_from)
    else:
        num_dec = num
    num_hex = dec_to_hex(num_dec)
    print(f"{num_sys_to}: ", *num_hex, sep="")
