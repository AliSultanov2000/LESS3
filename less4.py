# 4. Определить, какое число в массиве встречается чаще всего.

elements = list(map(int, input().strip().split()))
my_dict = {}
maxcnt = 0
for elem in elements:
    if elem not in my_dict:
        my_dict[elem] = 0
    my_dict[elem] += 1

for cnt in my_dict:
    if my_dict[cnt] > maxcnt:
        maxcnt = cnt
print(maxcnt)
