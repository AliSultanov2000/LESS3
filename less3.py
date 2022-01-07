# Задание 3
#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random
n = int(input("Количество элементов массива:"))
my_list = [random.randint(-10, 10) for i in range(n)]
print(my_list)
max_elem, min_elem = max(my_list), min(my_list)
my_list[my_list.index(max_elem)] = min_elem
my_list[my_list.index(min_elem)] = max_elem
print(my_list)

