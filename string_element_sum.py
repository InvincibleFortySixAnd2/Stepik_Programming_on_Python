# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его
# соседей. Для элементов списка, являющихся крайними, одним из соседей
# считается элемент, находящий на противоположном конце этого списка.
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка,
# разделёнными пробелом.

list = [int(l) for l in input().split()]
answer = ''
i = 0
k = i - 1
j = i + 1

if len(list) == 1:
    answer = str(list[0])
    print(answer)
else:
    for n in list:
        first_n = list[k]
        second_n = list[j]
        sum = first_n + second_n
        answer = answer + str(sum) + ' '
        i += 1
        k = i - 1
        j = i + 1
        if j == len(list):
            sum = list[k] + list[0]
            answer = answer + str(sum)
            break
    print(answer)
