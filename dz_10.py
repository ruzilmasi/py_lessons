# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной
# схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой
# матрицы складываем с первым элементом первой строки второй матрицы и пр.
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        res = ''
        for el in self.matrix_list:
            res += f'{el}\n'
        return res

    def __add__(self, other):
        sum_matrix_list = [[self.matrix_list[i][j] + other.matrix_list[i][j]
                            for j in range(len(self.matrix_list[0]))] for i in range(len(self.matrix_list))]
        return Matrix(sum_matrix_list)


m_1 = Matrix([[2, 4, 6], [9, 1, 8], [5, 3, 0]])
m_2 = Matrix([[10, 8, 6], [3, 11, 4], [7, 9, 12]])
m_3 = Matrix([[10, 8, 6], [3, 11, 4], [7, 9, 12]])

print(m_1 + m_2 + m_3)


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.


class Cloth(ABC):
    def __init__(self):
        pass
        # self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} {self.calc:.2f} m'

    @abstractmethod
    def calc(self):
        pass


class Coat(Cloth):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def calc(self):
        return self.v / 6.5 + 0.5


class Costume(Cloth):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def calc(self):
        return 2 * self.h + 0.3


class Main:
    def __init__(self):
        self.cloths = []

    def __str__(self):
        return f'Total size {self.total_cloth_consumption:.2f} m'

    def add_cloths(self, cloth):
        self.cloths.append(cloth)

    @property
    def total_cloth_consumption(self):
        total = 0
        for cloth in self.cloths:
            total += cloth.calc
        return total
        # return f'Total size {total:.2f} m'


main = Main()
cloth_1 = Coat(10)
print(cloth_1)

cloth_2 = Costume(20)
print(cloth_2)

main.add_cloths(cloth_1)
main.add_cloths(cloth_2)

# print(main.total_cloth_consumption())
print(main)


# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать
# класс «Клетка». В его конструкторе инициализировать параметр, соответствующий количеству ячеек
# клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества
# ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества
# ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек
# в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод
# make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order()
# вернёт строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f'{self.cells}'

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        result = Cell(self.cells - other.cells)
        if other.cells < self.cells:
            return result
        else:
            return f'Не верный результат'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __floordiv__(self, other):
        return Cell(self.cells // other.cells)

    def __truediv__(self, other):
        return Cell(self.cells / other.cells)

    def make_order(self, count):
        res = ''
        for c in range(self.cells // count):
            res += f"{'*' * count}\n"
        if self.cells % count > 0:
            res += f"{'*' * (self.cells % count)}"
        return res


# c_1 = Cell(5)
c_2 = Cell(10)
c_3 = Cell(20)
# print(c_1 + c_2 + c_3)
# print(c_3 - c_2)
# print(c_1 * c_2)
# print(c_3 // c_2)

# print(c_3.make_order(8))

c_4 = c_2 + c_3
print(c_4.make_order(8))
