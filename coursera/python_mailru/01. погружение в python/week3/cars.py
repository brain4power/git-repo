import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        # self.brand = brand
        # self.photo_file_name = photo_file_name
        # self.carrying = carrying
        pass

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if body_whl:
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
        else:
            self.body_whl = self.body_length = self.body_width = self.body_height = 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='UTF-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
           try:
                if row[0] == 'car' and '.' in row[3] and len(row[1]):
                    car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                elif row[0] == 'truck' and '.' in row[3] and len(row[1]):
                    car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                elif row[0] == 'spec_machine' and '.' in row[3] and len(row[1]):
                    car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
           except:
               pass
    return car_list


print(get_car_list('coursera_week3_cars.csv'))
# print(get_car_list('coursera_week3_cars.csv')[1].get_body_volume())

# Далее необходимо реализовать функцию, на вход которой подается имя файла в формате csv.
# Файл содержит данные аналогичные строкам из таблицы. Вам необходимо прочитать этот файл
# построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки и
# создать список нужных объектов с автомобилями и специальной техникой. Функция должна возвращать список объектов.
