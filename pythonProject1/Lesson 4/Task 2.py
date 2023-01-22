""" Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента."""


def my_func_2():
    user_answer = input().split()
    num = [int(_) for _ in user_answer]
    return [a for i, a in enumerate(num) if a > num[i - 1]]


print(my_func_2())
