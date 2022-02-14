# Программа считвает строку с числами и выводит их сумму.

list = [int(i) for i in input().split()]
sum = 0
for n in list:
    sum += n
print(sum)
