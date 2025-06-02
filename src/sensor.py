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

    @abstractmethod
    def _scan_plate(self):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        print(f"\n\nIncoming 🚘 vehicle detected. Plate: {plate}")
        if self.car_park.available_bays <= 0:
            print("Sorry this Car Park is now full. Try another Car Park or wait.")
        else :
            self.car_park.add_car(plate)

    def _scan_plate(self):   # Scan car plate ie generate car plate number
        return 'FAKE-' + format(random.randint(0, 999), "03d")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        print(f"\n\nOutgoing 🚗 vehicle detected. Plate: {plate}")
        self.car_park.remove_car(plate)

    def _scan_plate(self):   # Scan car plate ie generate car plate number from existing plates
        if len(self.car_park.plates) == 0 :
            print("There are no cars in this car park")
            return 0
        return random.choice(self.car_park.plates)