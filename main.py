from random import *


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= 100:
        return True
    return False


def is_valid_right_border(n):
    if n.isdigit():
        if int(n) >= 2:
            return True
    else:
        return False


def gen_rand_num():
    attempt_count = 0
    rn = input("Задайте целое число правой границы(n >= 2): ")
    while not is_valid_right_border(rn):
        rn = input("А может быть все-таки введем целое число больше и равно 2? ")
    rn = int(rn)
    num = randint(1, rn)
    return num, rn, attempt_count


print("Добро пожаловать в числовую угадайку")
num, rn, cnt = gen_rand_num()

while True:
    n = input(f"Введите число от 1 до {rn}: ")
    cnt += 1
    if not is_valid(n):
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    n = int(n)
    if n < num:
        print("Ваше число меньше загаданного, попробуйте еще разок")
        continue
    if n > num:
        print("Ваше число больше загаданного, попробуйте еще разок")
        continue
    print("Вы угадали, поздравляем!")
    print(f"Количество попыток: {cnt}")
    print()
    want = input("Желаете начать новую игру? (д = да, н = нет) ")
    if want.lower() == 'д':
        num, rn, cnt = gen_rand_num()
        continue
    break

print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
