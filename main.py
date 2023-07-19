def select_direction():
    direction = input("Выберите направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ")
    while direction != '+' and direction != '-':
        direction = input("Неверный ввод. Повторите: ")
    return direction


def select_language():
    language = input("Выберите язык: \n(en) - английский \n(ru) - русский:\n ")
    while language != 'en' and language != 'ru':
        language = input("Неверный ввод. Повторите: ")
    return language


def set_step():
    step = input("Напишите шаг сдвига(должен быть натуральное число):\n ")
    while not step.isdecimal():
        step = input("Неверный ввод. Повторите: ")
    return int(step)

def set_text():
    text = input('Какой текст нужно использовать сейчас? \n')
    while text.isspace():
        whats_text = input('Что-то не то ты ввёл. Введи текст. \n')
    return text

def caesar(direction, language, step, text):
    print('Программа шифровки/дешифровки текста по методу Цезаря')

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    if language == 'ru':
        alphas = 32
        low_alphabet = lower_rus_alphabet
        upp_alphabet = upper_rus_alphabet
    else:
        alphas = 26
        low_alphabet= lower_eng_alphabet
        upp_alphabet = upper_eng_alphabet

    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                place = upp_alphabet.index(text[i])
            else:
                place = low_alphabet.index(text[i])
            if direction == '+':
                index = (place + step) % alphas
            else:
                index = (place - step) % alphas
            if text[i].isupper():
                print(upp_alphabet[index], end='')
            else:
                print(low_alphabet[index], end='')
        else:
            print(text[i], end='')


caesar(select_direction(), select_language(), set_step(), set_text())
