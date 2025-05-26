import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):      # Print display Sensor
        return f"Sensor {self.id} is {self.is_active}."

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    def _scan_plate(self):   # Scan car plate ie generate car plate number
        # if entry sensor
        # return 'FAKE-' + format(random.randint(0, 999), "03d")
        # if exit sensor
        return random.choice(self.car_park.plates)

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")
