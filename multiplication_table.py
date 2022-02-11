# Программа считывает четыре числа до 10 и выводит таблицу
# перемножения этих чисел.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<=10 and b<=10 and c<=10 and d<=10 and a<=b and c<=d:

    # Формирование первой строки таблицы
    first_str = '\t'
    for k in range(c, d + 1):
        first_str = first_str + str(k) + '\t'
    print(first_str)

    # Основной цикл, который выводит каждую строку,
    # предоставленную вложенным циклом и передаёт
    # ему новое значение в интервале от 'a' до 'b'.
    for i in range(a, b + 1):
        ans = str(i) + '\t'

        # Цикл, который формирует каждую строку ответа,
        # умножая 'a' на 'c' и 'd'
        for j in range(c, d + 1):
            n = i * j
            ans = ans + str(n) + '\t'
            j += 1
        print(ans)
        i += 1
