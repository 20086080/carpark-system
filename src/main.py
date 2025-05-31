from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)

car_park = CarPark("moondalup",100,None,[],[])

entry_sensor = EntrySensor(1, car_park, True)
exit_sensor = ExitSensor(2, car_park, True)
entry_sensor1 = EntrySensor(3, car_park, True)
exit_sensor1 = ExitSensor(2, car_park, False)

display_one = Display("1",car_park,"Welcome to Moondalup",True)
display_two = Display("2",car_park,"Welcome to Moondalup",True)
display_three = Display("3",car_park,"Welcome to Moondalup",False)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(entry_sensor1)
car_park.register(exit_sensor1)
car_park.register(display_one)
car_park.register(display_two)
car_park.register(display_three)

print(f"\n{car_park}")

# If the above 3 are commented then the display does not come - why

#print(car_park.sensors[0], "\n", car_park.sensors[1], "\n",car_park.displays[0])
#print(car_park.sensors[0].is_active)
#print(dir(car_park.sensors[0]))

for itr in range(10):
    entry_sensor.detect_vehicle()

for itr in range(2):
    exit_sensor.detect_vehicle()
