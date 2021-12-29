import logging
logging.basicConfig(filename='calc_log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(funcName)s || %(message)s')

print("Զրոն որպես գործողության նշան կդադարեցնի ծրագիրը")

while True:
    operator = input("Operator (+,-,*,/): ")
    solution = 0
    if operator == '0':
        logging.info('Project ended')
        break
    if operator in ('+', '-', '*', '/'):
        num1 = int(input("number1 =  "))
        num2 = int(input("number2 =  "))
        logging.info(f'The user entered the numbers {num1} and {num2}')

        if operator == '+':
            solution = num1 + num2
        elif operator == '-':
            solution = num1 - num2
        elif operator == '*':
            solution = num1 * num2
        elif operator == '/':
            if num2 != 0:
                solution = num1 / num2
            else:
                print('Cannot be divided by zero')
                logging.error('Cannot be divided by zero')
                continue
        print(f"{num1} {operator} {num2} = {solution}")
        logging.info(f'The user entered the {operator} symbol')
        logging.info(f'{num1} {operator} {num2} = {solution}')
    else:
        print("Invalid operator")
        logging.error(f'Invalid operator {operator}')
