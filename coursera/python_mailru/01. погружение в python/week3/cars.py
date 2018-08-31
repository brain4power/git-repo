import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass
    def get_photo_file_ext(self, photo_file_name):
        #os.path.splitext
        pass


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        pass

    def get_body_volume(self):
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        pass


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if len(row) and (row[0] in ['car', 'truck', 'spec_machine']):
                print(row)
                if len(row) and (row[0] is 'car'):
                    pass
                elif len(row) and (row[0] is 'truck'):
                    pass
                elif len(row) and (row[0] is 'spec_machine'):
                    pass
            # else:
            #     pass
                # if row[0] is 'car':
                #     print('est odna!')
            #car_list.append(Car(row))
    return car_list

get_car_list('coursera_week3_cars.csv')




# Далее необходимо реализовать функцию, на вход которой подается имя файла в формате csv.
# Файл содержит данные аналогичные строкам из таблицы. Вам необходимо прочитать этот файл
# построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки и
# создать список нужных объектов с автомобилями и специальной техникой. Функция должна возвращать список объектов.
