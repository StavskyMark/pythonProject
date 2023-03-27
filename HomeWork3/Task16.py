'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5

1 2 3 4 5

3
-> 1
'''
import random

list_len = int(input('Введите размер массива: '))
my_list = [random.randint(0, 20) for i in range(list_len)]
print(my_list)

numb_x = int(input('Введите число x: '))
result = 0

for i in range(list_len):
    if my_list[i] == numb_x:
        result += 1

print(result)
