class CarPark:
    def __init__(self, location = "Unknown", capacity = "Unknown",
                 plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []      # empty list if value is None
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):      # Print Car_park object
        return f"Car Park at {self.location} , with {self.capacity} bays."

