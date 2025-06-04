import unittest
from car_park import CarPark
from sensor import Sensor, EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street",100)
        self.entry_sensor = EntrySensor(1, self.car_park,True)
        self.exit_sensor = ExitSensor(2, self.car_park,True)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.entry_sensor.car_park.capacity, 100)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park.location, "123 Example Street")

    def test_entry_sensor_part_of_sensor(self):
        self.assertIsInstance(self.entry_sensor, Sensor)

    def test_entry_sensor_detect_vehicle_scan_plate(self):
        self.entry_sensor.detect_vehicle()
        self.assertIn("FAKE", self.entry_sensor._scan_plate())

        # Checking message if no availability in Car Park
        self.entry_sensor.car_park.capacity = 0
        self.entry_sensor.detect_vehicle()
        self.assertIn("FAKE", self.entry_sensor._scan_plate())

    def test_exit_sensor_car_park_attributes(self):
        self.assertEqual(self.exit_sensor.car_park.capacity, 100)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.car_park.location, "123 Example Street")
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_exit_sensor_part_of_sensor(self):
        self.assertIsInstance(self.exit_sensor, Sensor)

    def test_exit_sensor_detect_vehicle_scan_plate(self):
        # Checking for empty Car Park message
        self.exit_sensor._scan_plate()
        # Checking for Car Park with cars
        self.exit_sensor.car_park.plates = ["FAKE-101","FAKE-102","FAKE-103"]
        self.exit_sensor.detect_vehicle()
        self.assertIn(self.exit_sensor._scan_plate(), self.exit_sensor.car_park.plates)

if __name__ == "__main__":
   unittest.main()