def my_print(*params, endl="\n"):
    print(*params, end=endl)


my_print(2, 54, 4)
my_print(34, 4, endl="\t")
my_print("Hello", endl=" ")
my_print("John")
my_print(27)
