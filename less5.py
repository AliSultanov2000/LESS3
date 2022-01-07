# Задание 5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве


list5 = list(map(int, input().strip().split()))
max_minus_elem = -9999999
for elem in list5:
    if elem < 0 and elem > max_minus_elem:
        max_minus_elem = elem

if max_minus_elem != -9999999:
    print(max_minus_elem)
    print(list5.index(max_minus_elem))
else:
    print("В массиве не нашлось отрицательных элементов")

