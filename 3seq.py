'''
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно
'''
str_num_1 = input('Введите 1й список чисел через запятую ')
str_num_2 = input('Введите 2й список чисел через запятую ')
lst_num_1 = str_num_1.split(',')
lst_num_2 = str_num_2.split(',')
for item in lst_num_1:
    if item not in lst_num_2:
        print(f'{item}', end=' ')
