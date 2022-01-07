# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random
m, n = map(int, input("Введите размер матрицы").strip().split())
matrix = [[random.randint(-10, 10) for j in range(n)] for i in range(m)]
list_of_min_elements = []  # список минимальных элементов столбцов матрицы
for i in range(n):
    minelement = 1000
    for j in range(m):
        if matrix[j][i] < minelement:
            minelement = matrix[j][i]
    list_of_min_elements.append(minelement)


max_result = -1000
for element in list_of_min_elements:
    if element > max_result:
        max_result = element
print(f'Ответ: {max_result}')  # это является ответом
print(list_of_min_elements)

# выведем также саму матрицу
s = ""
for k1 in matrix:
    for k2 in k1:
        s += " " + str(k2)
    s += "\n"
print(s)
