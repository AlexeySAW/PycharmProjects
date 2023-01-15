""" Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(arg_1, arg_2, arg_3):
    arr = [arg_1, arg_2, arg_3]
    a = list(filter(lambda x: x != max(arr), arr))
    return max(arr) + max(a)


print(my_func(7, 15, 30))
