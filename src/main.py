from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# Create a car park
car_park = CarPark("moondalup",
                   100,
                   None,
                   [],
                   [],
                   "moondalup.txt",
                   "moondalup_config.json")

car_park.write_config() # Write car park configuration to json
car_park = car_park.from_config(car_park.config_file)  # Re-create car park from json file

# Create Sensors and Display
entry_sensor = EntrySensor(1, car_park, True)
exit_sensor = ExitSensor(2, car_park, True)
display_one = Display("1",car_park,"Welcome to Moondalup",True)

# Register Sensors and Display to car park
car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display_one)

print(f"\n{car_park}")   # Print car park

# Add 10 cars into car park
for itr in range(10):
    entry_sensor.detect_vehicle()

# Remove 2 cars from car park
for itr in range(2):
    exit_sensor.detect_vehicle()
