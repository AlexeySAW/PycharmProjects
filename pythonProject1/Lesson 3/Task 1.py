"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(arg):
    try:
        dividend, divider = [int(_) for _ in arg]
        return f'{dividend / divider:.2f}'
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    except ValueError:
        print('Не хватает значения')


print(division(input('Введите делимое и делитель: ').split()))
