'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
1 2 3 4 5

6

-> 5
'''

list_len = int(input('Введите длину массива: '))
my_list = [i for i in range(list_len)]
print(my_list)

numb_x = int(input('Введите число x: '))
number = 0

for i in range(list_len):
    if numb_x - my_list[i] < numb_x - number and numb_x - my_list[i] > 0:
        number = i

print(my_list[number])


