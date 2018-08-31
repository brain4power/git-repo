class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass
    def get_photo_file_ext(self):
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
    return car_list