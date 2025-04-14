import unittest
import math


def summa (first, second):

    return first + second


def sub (first, second):

    return first - second


def mult (first, second):

    return first * second


def div (first, second):

    return first / second


def calc(first, second, oper):

    result = None

    if oper == '+':

        result = summa(first, second)

    elif oper == '-':

        result = sub(first, second)

    elif oper == '*':

        result = mult(first, second)

    elif oper == '/':

        if (second == 0):

            print('Деление на ноль запрещено!')

            return

        result = div(first, second)

    elif oper == '%':

        result = first / second * 100

    elif oper == '**':

        result = first ** second

    elif oper == 'log':

        result = math.log(first, second)

    else:

        print('Некорректная операция!')

    return result


def operation():

    mes = input('Выберите операцию (Введите +, -, *, /, %, **, log):\n '

                '+ - сложение двух чисел\n'

                '- - вычитание двух чисел\n'

                '* - умножение двух чисел\n'

                '/ - деление двух чисел\n'

                '% - процент первого числа от второго\n'

                '** - возведение первого числа в степень второго\n'

                'log - логарифм первого числа по основанию второго\n')

    if mes == '+':

        print('Вы выбрали сумму')

    elif mes == '-':

        print('Вы выбрали разность')

    elif mes == '*':

        print('Вы выбрали умножение')

    elif mes == '/':

        print('Вы выбрали деление')

    elif mes == '%':

        print('Вы выбрали нахождение процента первого числа от второго')

    elif mes == '**':

        print('Вы выбрали возведение в степень')

    elif mes == 'log':

        print('Вы выбрали логарифм')


    correct_operations = ['+', '-', '*', '/', '%', '**', 'log']

    while mes not in correct_operations:

        print('Такой операции нет в списке. Попробуйте ещё!')

        mes = input()


    return mes


def run():

    try:

        first = int(input('Укажите первое число: '))

    except ValueError:

        first = int(input('Вы ввели некорректные данные. Пожалуйста, введите целое число.'))

    try:

        second = int(input('Укажите второе число: '))

    except ValueError:

        second = int(input('Вы ввели некорректные данные. Пожалуйста, введите целое число.'))

    op = operation()

    result = calc(first, second, op)

    print(f'Результат: {result}')


progam_is_running = False

while(progam_is_running):

    run()

    answer = input('Желаете продолжить?\n'

      ' Введите + если да и прочий символ, если нет: ')

    if answer != '+':

        progam_is_running = False

class TestCalculatingMethods(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(summa(15, 6), 21)

    def test_sub(self):
        self.assertEqual(sub(15, 6), 9)

    def test_mult(self):
        self.assertEqual(mult(5, 5), 25)
    
    def test_mult(self):
        self.assertEqual(div(5, 5), 1)

if __name__ == '__main__':
    unittest.main()