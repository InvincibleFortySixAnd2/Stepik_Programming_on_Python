# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки
# сначала максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a >= c):
    max = a
elif (b >= c) and (b >= a):
    max = b
else:
    max = c

if (a <= b) and (a <= c):
    min = a
elif (b <= c) and (b <= a):
    min = b
else:
    min = c

lost = (a + b + c) - (max + min)

print(str(max))
print(str(min))
print(str(lost))
