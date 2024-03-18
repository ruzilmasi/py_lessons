# 1. Написать функцию email_parse(<email_address>), которая при помощи
# регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает
# их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
# выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
import re

RE_NAME = re.compile(r'^([\w.-]+)@([\w.-]+)$', re.IGNORECASE)


def email_parse(mail):
    res_dict = {}
    res = RE_NAME.findall(mail)
    username = res[0][0]
    domain = res[0][1]
    res_dict['username'] = username
    res_dict['domain'] = domain
    return res_dict


print(email_parse('someone@geekbrains.ru'))

# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
#     5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы
# вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли
# вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fin = []
        res = func(*args, **kwargs)
        for arg in args:
            fin.append(f'{func.__name__}({arg}: {type(arg)} - {type(res)})')
        for kwarg in kwargs.values():
            fin.append(f'{func.__name__}({str(kwarg)}: {type(kwarg)} - {type(res)})')
        return ', '.join(fin)
    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    res_list = []
    for arg in args:
        res_list.append(arg ** 3)
    return res_list


a = calc_cube(5, 14, f=88.6)
print(a)


# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(el):
            if callback(el):
                res = func(el)
            else:
                raise ValueError(f'wrong val {el}')
            return res
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


# a = calc_cube(5)
b = calc_cube(-7)
print(b)
# help(calc_cube)
