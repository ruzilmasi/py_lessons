# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского
# на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
import random


def num_translate(num, transl):
    if num in transl:
        return transl[num]
    else:
        return None


translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'fifth': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
print(num_translate('nine', translate))

# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate_adv(num, transl):
    num = str(num)
    if num in transl:
        return transl[num]
    elif num.capitalize():
        if num.lower() in transl:
            res = transl[num.lower()]
            return res.capitalize()
    else:
        return None


print(num_translate_adv('Seven', translate))

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся
# с соответствующей буквы. Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?


def thesaurus(*args):
    nms = {}
    for name in args:
        key = name[0]
        if key in nms:
            nms[key].append(name)
        else:
            nms[key] = [name]
    return nms


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи - первые буквы фамилий,
# а значения - словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    sur_nms = {}
    for el in args:
        name = el.split()[0]
        sur_name = el.split()[1]
        key_name = name[0]
        key_surname = sur_name[0]
        if key_surname in sur_nms:
            res = sur_nms[key_surname]
            if key_name in res:
                res[key_name].append(el)
            else:
                res[key_name] = [el]
        else:
            sur_nms[key_surname] = {key_name: [el]}

    sorted_keys = sorted(sur_nms.keys())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = sur_nms[key]
    return sorted_dict


print(thesaurus_adv("Петр Алексеев", "Иван Сергеев", "Инна Серова", "Илья Иванов", "Анна Савельева"))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


# def get_jokes(a, b, c, count):
#     res_list = []
#     for i in range(count):
#         res = f'{random.choice(a)} {random.choice(b)} {random.choice(c)}'
#         res_list.append(res)
#     return res_list


def get_jokes(a, b, c, count, flag=False):
    res_list = []
    if flag and count > 5:
        print('Макс количество неповторяющихся шуток не больше 5 bitch!')
    for i in range(count):
        if flag:
            if count <= 5:
                random.shuffle(a)
                random.shuffle(b)
                random.shuffle(c)
                res = f'{a.pop()} {b.pop()} {c.pop()}'
                res_list.append(res)
        else:
            res = f'{random.choice(a)} {random.choice(b)} {random.choice(c)}'
            res_list.append(res)
    return res_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(nouns, adverbs, adjectives, 5, flag=True))
