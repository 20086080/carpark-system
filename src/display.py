class Display:
    def __init__(self, id : str, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):      # Print display object
        return f"Display {self.id} : Welcome to {self.car_park}."

    def update(self, data):           #
        for key, value in data.items():
            print(f"{key}: {value}", end = "    ")