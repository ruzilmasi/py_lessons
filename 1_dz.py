# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
#
# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода
# сразу для нескольких значений продолжительности, будет ли тут полезен список?

duration = 53

seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 60 // 60 % 24
days = duration // 60 // 60 // 24

if days != 0:
    print(f'{days} дн {hours} час {minutes} мин  {seconds} сек')
elif hours != 0:
    print(f'{hours} час {minutes} мин  {seconds} сек')
elif minutes != 0:
    print(f'{minutes} мин {seconds} сек')
elif seconds != 0:
    print(f'{seconds} сек')




# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например,
# число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# res_list = 0
# is_uneven = []
#
# for i in range(1, 1000, 2):
#     is_uneven.append(i**3 + 17)
#
# for j in is_uneven:
#     el = j
#     number = 0
#     while j != 0:
#         number += j % 10
#         j = j // 10
#     if number % 7 == 0:
#         res_list += el
#
# print(res_list)
# # ------------------------------------------------
iterable = 0
sum_number = 0

for i in range(1, 1000, 2):
    iterable += i ** 3 + 17
    j = iterable
    number = 0
    while iterable != 0:
        num = iterable % 10
        number += num
        iterable = iterable // 10
    if number % 7 == 0:
        sum_number += j

print(sum_number)

# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой
# для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(f'{i} процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        if 10 < i < 20:
            print(f'{i} процентов')
        else:
            print(f'{i} процента')
    else:
        print(f'{i} процентов')