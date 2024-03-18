# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить
# соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for i in range(len(self.__color)):
                if i == 0:
                    print(self.__color[i])
                    time.sleep(5)
                elif i == 1:
                    print(self.__color[i])
                    time.sleep(2)
                elif i == 2:
                    print(self.__color[i])
                    time.sleep(4)


t = TrafficLight()
t.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_method(self, weight=0, thickness=0):
        res = self._length * self._width * weight * thickness
        print(f'{res//1000} т')


r = Road(20, 5000)
r.calc_method(25, 5)

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


p = Position('Ivan', 'Zubkov', 'Слесарь', {'wage': 50000, 'bonus': 23000})
p.get_full_name()
p.get_total_income()

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go,
# stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'Машина {self.name} {self.color} цвета поехала')

    def stop(self):
        print(f'Машина {self.name} {self.color} остановилась')

    def turn(self, direction='влево'):
        print(f'Машина {self.name} {self.color} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color, name, speed=60):
        super().__init__(speed, color, name)
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, color, name, speed=40):
        super().__init__(speed, color, name)
        if speed > 40:
            print('Помедленее')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        if is_police:
            print('Police Car')


t = TownCar('серый', 'Skoda Rapid', 62)
t.go()
t.stop()
t.turn('вправо')
t.show_speed()

w = WorkCar('Желтый', 'VolksWagen Polo', 62)
w.show_speed()

p = PoliceCar(120, 'Черный', 'Ford Focus')
p.turn()


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск
# отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} обычно хорошо пишет в тетради')


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'Ну {self.title}ом пишут временно или рисуют')


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'Чаще всего {self.title}ом делают пометки на коробках и в строительстве')


pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Маркер')
handle.draw()
