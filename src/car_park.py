from sensor import Sensor
from display import Display
from datetime import datetime


class CarPark:
    def __init__(self, location = "Unknown", capacity = 0,
                 plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []      # Car plates in the carpark
        self.sensors = sensors or []    # List of sensors in the carpark
        self.displays = displays or []  # List of displays in the carpark

    @property
    def available_bays(self):
        return self.capacity - len(self.plates) \
            if len(self.plates) <  self.capacity else 0         # Check car_park not full

    def __str__(self):      # Print Car_park object
        return (f"Car Park at {self.location}, with total "
                f"{self.capacity} bays, {len(self.sensors)} active Sensor(s) "
                f"and {len(self.displays)} active Display(s)")

    def register(self, component)  :  #fix    Allow the car park to register sensors and displays (component will be either)
        if isinstance(component, Sensor):
            if component.is_active : self.sensors.append(component)
        elif isinstance(component, Display):
            if component.is_on : self.displays.append(component)
        else:
            raise TypeError("Object must be a Sensor or Display")

    def add_car(self, plate) : # When a car enters the car park - record the plate number and update the displays.
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate) : # When car exits the car park - remove the plate number and update the displays.
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self) : # When car park needs to update the displays.
        data = {"Available bays": self.available_bays, "Temperature": 25,
                "Date": datetime.now().date(),"Time": datetime.now().time()}
        for display in self.displays:
            print(f"\n{display}")
            display.update(data)

