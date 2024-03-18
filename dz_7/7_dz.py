#  Работа с файловой системой. Исключения в Python
# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
# конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

ROOT = os.path.dirname(__file__)
dir_name = 'my_project'
dir_name2 = ('settings', 'mainapp', 'adminapp', 'authapp')


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


full_path = os.path.join(ROOT, dir_name)
create_folder(full_path)

for el in dir_name2:
    dir_path = os.path.join(dir_name, el)
    create_folder(dir_path)

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import yaml

HOME = os.path.split(os.path.abspath(__file__))[0]


def make_dirs(path, list_dir):
    for i in list_dir:
        if not os.path.exists(i):
            os.mkdir(i)
        if type(list_dir) is dict:
            for j in list_dir[i]:
                work_dir = os.path.join(path, i)
                os.chdir(work_dir)
                if type(j) is dict:
                    make_dirs(work_dir, j)
                else:
                    if len(j.split('.')) == 2:
                        if not os.path.exists(j):
                            with open(j, 'w', encoding='utf-8') as file:
                                file.close()


with open('config.yaml') as f:
    list_dir = yaml.safe_load(f)            #читаем из yaml


make_dirs(HOME, list_dir)

# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import shutil
HOME = os.path.split(os.path.abspath(__file__))[0]

root_dir = os.path.join(HOME, 'my_project')
dst_dir = os.path.join(HOME, 'my_project', 'templates')

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)                        #создаем папку templates

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir_ in dirs:                       #проходимся по содержимому в templates
            if not os.path.exists(os.path.join(dst_dir, dir_)):
                os.makedirs(os.path.join(dst_dir, dir_))            #создаем такую же папку в новом templates
        for file in files:
            src_file = os.path.join(root, file)                     #старый путь к файлу, откуда надо копировать
            dst_file = os.path.join(dst_dir, os.path.basename(root))    #новый путь к файлу, куда надо копировать
            if not os.path.dirname(src_file) == dst_file:
                shutil.copy(src_file, dst_file)                     #копируем файл
