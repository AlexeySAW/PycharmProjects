""" Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения."""

from itertools import count, cycle


def my_func():
    l = []
    ex = 0
    for el in count(3):
        if el > 10:
            break
        l.append(el)
    for i in cycle(l):
        if ex > 20:
            break
        ex += 1
        print(i)


my_func()
