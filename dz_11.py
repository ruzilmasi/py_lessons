# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в
# виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу
# «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import datetime
import time


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def set_data(cls, f_str):
        day, month, year = f_str.split('-')
        return cls([int(day), int(month), int(year)])

    @staticmethod
    def validation(dat):
        try:
            datetime.datetime.strptime(dat, '%d-%m-%Y')
        except ValueError:
            return f'Incorrect'
        else:
            return f'Correct!'


d_1 = Data.set_data('22-01-2023')
print(d_1.date)
d_2 = Data.validation('12-02-2020')
print(d_2)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его
# работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyOwnErr(Exception):
    pass


x, y = input('Enter two numbers: ').split(' ')
try:
    if int(y) == 0:
        raise MyOwnErr('Only nums > 0')
    res = int(x) // int(y)
except ValueError as err:
    print('Value error !!')
except MyOwnErr as err:
    print(err)
else:
    print(res)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
# только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные
# и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна
# завершаться.


class NotNumberError(Exception):
    pass


number_list = []
while True:
    try:
        element = input('enter a number: ')
        if element == 'stop':
            print(number_list)
            break
        if not element.isdigit():
            raise NotNumberError('this is not a number')
        number_list.append(int(element))
    except NotNumberError as err:
        print(err)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых
# типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

from abc import ABC, abstractmethod


class ValidationErr(Exception):
    pass


class Storage:
    def __init__(self):
        self.bill = {}

    def __str__(self):
        show = ''
        for key, val in self.bill.items():
            show += f'{key}: {val}\n'
        return show

    def add_office_equipment(self, equipment, count):
        try:
            if type(count) is not int:
                raise ValidationErr('Err: count is only integer!')
        except ValidationErr as err:
            print(err)
        else:
            if count > 0:
                if equipment in self.bill:
                    self.bill[equipment] += count
                else:
                    self.bill[equipment] = count

    def transfer(self, equipment, count, unit):
        if equipment in self.bill and count > 0:
            self.bill[equipment] -= count
            print(f'"{equipment.model}" to transfer - > {unit} with count: {count}')
        else:
            print('This product not in Storage')


class OfficeEquipment(ABC):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    @abstractmethod
    def __str__(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model, price, type_of_printer, max_format_of_paper,):
        super().__init__(model, price)
        self.type_of_printer = type_of_printer
        self.max_format_of_paper = max_format_of_paper

    def __str__(self):
        return f'{self.__class__.__name__}: {self.model} = {self.price} rub, {self.type_of_printer}-type, {self.max_format_of_paper}-format'


class Scaner(OfficeEquipment):
    def __init__(self, model, price, type_of_scaner, speed):
        super().__init__(model, price)
        self.type_of_scaner = type_of_scaner
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}: {self.model} = {self.price} rub, {self.type_of_scaner}-type, {self.speed} sec/list'


class Xerox(OfficeEquipment):
    def __init__(self, model, price, count_of_copies, scaling):
        super().__init__(model, price)
        self.count_of_copies = count_of_copies
        self.scaling = scaling

    def __str__(self):
        return f'{self.__class__.__name__}: {self.model} = {self.price} rub, {self.count_of_copies} lists/min, {self.scaling}-format'


oe_1 = Printer('Epson', 34890, 'laser', 'A3')
oe_1_1 = Printer('Samsung', 22222, 'jet', 'A4')
oe_2 = Scaner('Kyocera', 76899, 'tablet', 10)
oe_3 = Xerox('HP', 23999, 499, 'A4')
s = Storage()

s.add_office_equipment(oe_1, 50)
s.add_office_equipment(oe_1_1, 40)
s.add_office_equipment(oe_2, 10)
s.add_office_equipment(oe_3, 5)

s.transfer(oe_1_1, 39, 'Samara-Storage')
print(s)

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f'{self.real}+{self.imaginary}i'
        else:
            return f'{self.real}-{abs(self.imaginary)}i'

    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(r, i)


cn_1 = ComplexNumber(5, 10)
cn_2 = ComplexNumber(3, -2)

print(cn_1 + cn_2)
print(cn_1 * cn_2)
