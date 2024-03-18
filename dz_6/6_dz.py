# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
# список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
import json
import sys
import requests

responce = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = responce.text

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    paragraphs = content.splitlines()


def pars_file(pars):
    for el in pars:
        remote_addr = el.split()[0]
        request_type = el.split()[5][1:]
        requested_resource = el.split()[6]
        yield remote_addr, request_type, requested_resource


res = pars_file(paragraphs)
print(next(res))
print(next(res))
print(next(res))

# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
# из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

responce = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = responce.text

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(content)

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    paragraphs = content.splitlines()

spam_dict = {}
for el in paragraphs:
    if el.split()[0] in spam_dict:
        spam_dict[el.split()[0]] += 1
    else:
        spam_dict[el.split()[0]] = 1

max_val = max(spam_dict.values())
final_result = (k for k, v in spam_dict.items() if v == max_val)
print(*final_result)

# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много
# раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

info_dict = {}
with open('users.csv', 'r', encoding='utf-8') as f3:
    with open('hobby.csv', 'r', encoding='utf-8') as f4:
        users = (el for el in f3.read().splitlines())
        hobbies_data = (el for el in f4.read().splitlines())
        for hobbies, user in zip(hobbies_data, users):
            info_dict[user.strip().replace(',', ' ')] = hobbies.strip()
        for _ in hobbies_data:
            sys.exit(1)
        for user in users:
            info_dict[user.strip().replace(',', ' ')] = None
print(info_dict)

with open('info.json', 'w', encoding='utf-8') as f5:
    json.dump(info_dict, f5, ensure_ascii=False)


with open('users.csv', 'r', encoding='utf-8') as f:
    with open('hobby.csv', 'r', encoding='utf-8') as f2:
        users_content = f.read()
        hobbys_content = f2.read()

users_list = []
hobbys_list = []
for el in users_content.split('\n'):
    users_list.append(' '.join(el.split(',')))
for el in hobbys_content.split('\n'):
    hobbys_list.append(' '.join(el.split(',')))
data_dict = {str(i): j if len(users_list) >= len(hobbys_list) else exit(1) for i, j in itertools.zip_longest(users_list, hobbys_list)}

with open('data_file.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f)

with open('data_file.json', 'r', encoding='utf-8') as f:
    res = json.load(f)

print(res)


# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать
# парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби:
# преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа.
# Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в
# результате парсинга.

with open('users.csv', 'r', encoding='utf-8') as f6:
    with open('hobby.csv', 'r', encoding='utf-8') as f7:
        with open('users_hobby.txt', 'w', encoding='utf-8') as f8:
            for line1 in f6:
                line2 = f7.readline().strip()
                if not line2:
                    line2 = None
                f8.write(f'{line1.strip()}: {line2}\n')
            content = f7.readline()
            if content:
                sys.exit(1)


# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь
# к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
# когда все файлы находятся в разных папках.

f_name1 = sys.argv[1]
f_name2 = sys.argv[2]
f_name3 = sys.argv[3]

with open(f_name1, 'r', encoding='utf-8') as f11:
    with open(f_name2, 'r', encoding='utf-8') as f12:
        with open(f_name3, 'w', encoding='utf-8') as f13:
            for line1 in f11:
                line2 = f12.readline().strip()
                if not line2:
                    line2 = None
                f13.write(f'{line1.strip()}: {line2}\n')
            content = f12.readline()
            if content:
                sys.exit(1)

# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с
# интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. При записи
# передавать из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке
# следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
