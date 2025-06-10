from sensor import Sensor
from display import Display
from datetime import datetime
from pathlib import Path


class CarPark:
    def __init__(self, location = "Unknown", capacity = 0,
                 plates = None, sensors = None, displays = None, log_file = Path("log.txt")):
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
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

    def add_car(self, plate) : # When a car enters the car park - record the plate | update the displays.
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate) : # When car exits the car park - remove the plate | update the displays.
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "removed")

    def update_displays(self) : # When car park needs to update the displays.
        data = {"Available bays": self.available_bays, "Temperature": 25,
                "Date": datetime.now().date(),"Time": datetime.now().time()}
        for display in self.displays:
            print(f"\n{display}")
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")