from car_park import CarPark
from sensor import EntrySensor, ExitSensor, Sensor
from display import Display


# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)


def update_car_park(plate):
    pass

car_park = CarPark("moondalup",100,None,[],[])

entry_sensor = EntrySensor(1, car_park, True)
exit_sensor = ExitSensor(2, car_park, True)

display_one = Display("1",car_park,"Welcome to Moondalup",True)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display_one)

#print(car_park.sensors[0], "\n", car_park.sensors[1], "\n",car_park.displays[0])
#print(car_park.sensors[0].is_active)
#print(dir(car_park.sensors[0]))

for itr in range(10):
    entry_sensor.detect_vehicle()
print("\n",car_park.plates)

for itr in range(2):
    exit_sensor.detect_vehicle()
print("\n", car_park.plates)
