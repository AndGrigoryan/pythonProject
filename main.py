from random import *


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # head, torso, both arms, one leg
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # head, torso, both arms
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # head, torso and one arm
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # head and torso
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # head
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # initial state
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


world_list = ['Москва', 'Париж', 'Лондон', 'Рим', 'Токио', 'Берлин', 'Амстердам', 'Вашингтон', 'Сидней', 'Каир',
              'Мадрид', 'Дублин', 'Пекин', 'Афины', 'Стамбул', 'Рио-де-Жанейро', 'Копенгаген', 'Санкт-Петербург',
              'Венеция', 'Киев', 'Осло', 'Сеул', 'Вена', 'Ришон-Ле-Цион', 'Барселона', 'Мельбурн', 'Гонконг',
              'Сингапур', 'Прага', 'Киото', 'Канберра', 'Сан-Франциско', 'Шанхай', 'Рига', 'Астана', 'Будапешт',
              'Варшава', 'Копенгаген', 'Атланта', 'Лос-Анджелес', 'Сиэтл', 'Ванкувер', 'Монреаль', 'Чикаго',
              'Санкт-Луис', 'Торонто', 'Бостон', 'Майами', 'Сидней', 'Мумбаи', 'Дели', 'Бангкок', 'Дакка', 'Дубай',
              'Найроби', 'Кейптаун', 'Йоханнесбург', 'Каир', 'Лагос', 'Мехико', 'Рио-де-Жанейро', 'Сантьяго', 'Лима',
              'Каракас', 'Сан-Паулу', 'Лимассол', 'Аддис-Абеба', 'Киншаса', 'Нью-Йорк', 'Лас-Вегас', 'Торонто', 'Берн',
              'Афины', 'Брюссель', 'Варшава', 'Рига', 'Таллин', 'Минск', 'Белград', 'Сараево', 'Загреб', 'Любляна',
              'Бухарест', 'София', 'Лиссабон', 'Мадрид', 'Барселона', 'Валенсия', 'Севилья', 'Малага', 'Гранада',
              'Харьков', 'Донецк', 'Одесса', 'Кишинев', 'Вильнюс', 'Тбилиси', 'Ереван', 'Ашхабад', 'Астана', 'Алматы',
              'Душанбе']

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-"


def get_word():
    return choice(world_list).upper()


def validate_guessed_word_symbol():
    while True:
        word = input("Введите букву или целое слово:\n").upper()
        if len(word) > 1:
            for i in word:
                if i not in alphabet:
                    break
            else:
                return word, True
        if word in alphabet:
            return word, False
        else:
            print("Неверный ввод. Повторите: ")


def play(word):
    print('Давайте играть в угадайку слов!')
    word_completion = ('_ ' * len(word)).split()
    guessed = False
    guessed_letters = []
    guessed_words = []
    word_copy = word
    tries = 6
    print(display_hangman(tries))
    while tries != 0:
        guess, is_word = validate_guessed_word_symbol()
        if guess not in guessed_words and guess not in guessed_letters:
            if not is_word:
                guessed_letters.append(guess)
                if guess in word_copy:
                    while word_copy.find(guess) != -1:
                        word_completion[word_copy.find(guess)] = guess
                        word_copy = word_copy.replace(guess, ' ', 1)
                    print(word_completion)
                else:
                    tries -= 1
                    print(display_hangman(tries))
            else:
                guessed_words.append(guess)
                if guess == word:
                    guessed = True
                    break
                else:
                    tries -= 1
                    print(display_hangman(tries))
        else:
            print("Данное слово или букву вы раньше уже ввели, введите другое буква или слово целиком:\n")
            print(f"Уже введенные буквы: {guessed_letters}\nУже введенные слова: {guessed_words}")
            print(word_completion)
        if "_" not in word_completion:
            break
    else:
        print("К сожалению Вы проиграли.")
        print(f"Загаданное слово было: {word}")
    if guessed:
        print(f"Поздравляем Вы выиграли!!\nЗагаданное слово было: {word}\n")


play(get_word())
print("Хотите играть еще?(Да\\нет)\n")
want = input().lower()
while want == 'да':
    play(get_word())
    print("Хотите играть еще?(Да\\нет)\n")
    want = input().lower()
