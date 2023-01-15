"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге есть элементы с одинаковыми значениями, то новый элемент с тем же значением размещется после них."""

my_list = [7, 5, 3, 3, 2]

a = False
while not a:
    try:
        new_score = int(input('New score is: '))
        if new_score < 0:
            print('Должно быть положительное число')
            continue
        if new_score > max(my_list):
            my_list.insert(0, new_score)
            break
        if new_score < min(my_list):
            my_list.append(new_score)
            break
        for i, el in enumerate(my_list):
            if my_list[-1] == new_score:
                my_list.append(new_score)
                a = True
                break
            if el == new_score and el != my_list[i + 1]:
                my_list.insert(i + 1, new_score)
                a = True
                break
    except ValueError:
        print('Должно быть положительное число')

print(f'Измененный список {my_list}')
