class Sensor:
    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def __str__(self):      # Print display Sensor
        return f"Sensor {self.id} is {self.is_active}."

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass
