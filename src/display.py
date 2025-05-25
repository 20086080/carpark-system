class Display:
    def __init__(self, id, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):      # Print display object
        return f"Display {self.id} : Welcome to car park {self.car_park}."
