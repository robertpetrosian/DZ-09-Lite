'''
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]'''

lst_num =[]
kol = int(input('Введите размер списка '))
for i in range(kol):
    elem = int(input('Введите элемент списка '))
    lst_num.append(elem)

lst_num.sort()
print(lst_num)
