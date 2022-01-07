# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

m, n = 5, 4
main_list = []
for i in range(m):
    inner_list = list(map(int, input("Введите элементы массива").split(maxsplit=n - 1)))
    sum = 0
    for elem in inner_list:
        sum += elem
    inner_list.append(sum)
    main_list.append(inner_list)

#Выводим массив на экран
s = ""
for k1 in main_list:
    for k2 in k1:
        s += " " + str(k2)
    s += "\n"

print(s)

