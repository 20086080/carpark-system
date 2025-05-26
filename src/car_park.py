from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location = "Unknown", capacity = 0,
                 plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []      # empty list if value is None
        self.sensors = sensors or []
        self.displays = displays or []

    @property
    def available_bays(self):
        return self.capacity - len(self.plates) \
            if len(self.plates) <  self.capacity else 0         # Check car_park not full

    def __str__(self):      # Print Car_park object
        return f"Car Park at {self.location} , with {self.capacity} bays."

    def register(self, component)  :  # Allow the car park to register sensors and displays (component will be either)
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
        else:
            raise TypeError("Object must be a Sensor or Display")

    def add_car(self, plate) : # When a car enters the car park - record the plate number and update the displays.
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate) : # When car exits the car park - remove the plate number and update the displays.
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self) : # When car park needs to update the displays.
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)
