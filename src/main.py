from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: Write the car park configuration to a file called "moondalup_config.json"
# TODO: Reinitialize the car park object from the "moondalup_config.json" file
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)

car_park = CarPark("moondalup",
                   100,
                   None,
                   [],
                   [],
                   "moondalup.txt",
                   "moondalup_config.json")

car_park.write_config()
car_park = car_park.from_config(car_park.config_file)


entry_sensor = EntrySensor(1, car_park, True)
exit_sensor = ExitSensor(2, car_park, True)
display_one = Display("1",car_park,"Welcome to Moondalup",True)
car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display_one)


print(f"\n{car_park}")

for itr in range(10):
    entry_sensor.detect_vehicle()

for itr in range(2):
    exit_sensor.detect_vehicle()
