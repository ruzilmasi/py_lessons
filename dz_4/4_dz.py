# 1. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать
# результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
# передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
import decimal
import requests


def currency_rates(val):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = resp.text
    va = val.upper()
    if va in content:
        need_info = content.split(va)[1:]
        for el in str(need_info).split('<Value>')[1:2]:
            res = el.split('</Value>')[0].replace(',', '.')
            # return f'1 {va} = {round(float(res), 2)} руб'
            return f'1 {va} = {round(decimal.Decimal(res), 2)} руб'
    else:
        return None


print(currency_rates('EUR'))
print(currency_rates('usd'))

# 2. * (вместо 1) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?


def currency_rates(val):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = resp.text
    for date in content.split('Date="')[1:]:
        print(date.split('"')[0])
    va = val.upper()
    if va in content:
        need_info = content.split(va)[1:]
        for el in str(need_info).split('<Value>')[1:2]:
            res = el.split('</Value>')[0].replace(',', '.')
            return f'1 {va} = {round(decimal.Decimal(res), 2)} руб'
    else:
        return None


if __name__ == '__main__':
    print(currency_rates('GBP'))


# 3. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

# смотри файл: utils.py

# 4. * (вместо 3) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05
import sys


def currency_rates(val):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = resp.text
    for date in content.split('Date="')[1:]:
        print(date.split('"')[0])
    va = val.upper()
    if va in content:
        need_info = content.split(va)[1:]
        for el in str(need_info).split('<Value>')[1:2]:
            res = el.split('</Value>')[0].replace(',', '.')
            return f'1 {va} = {round(decimal.Decimal(res), 2)} руб'
    else:
        return None


if __name__ == '__main__':
    print(currency_rates(sys.argv[1]))
