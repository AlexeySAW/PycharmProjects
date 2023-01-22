""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """


def rewrite_file():
    try:
        with open('filsse.txt', 'r+') as file:
            file.write(input('Введите числа через пробел: '))
            a = map(int, file.read().split())
            print(sum(a))
    except FileNotFoundError:
        return 'Файл не найден.'


rewrite_file()
