# Программа считывающая с пользовательского ввода целое
# неотрицательное число и выводящая это число в консоль
# вместе с правильным образом изменённым словом "программист".
# Диапазон корректных чисел от 0 до 1000.

n = int(input())

if (n % 10 == 1) and (n % 100 != 11):
    print(str(n) + ' программист')
elif (n % 10 == 2) and (n % 100 != 12):
    print(str(n) + ' программиста')
elif (n % 10 == 3) and (n % 100 != 13):
    print(str(n) + ' программиста')
elif (n % 10 == 4) and (n % 100 != 14):
    print(str(n) + ' программиста')
else:
    print(str(n) + ' программистов')