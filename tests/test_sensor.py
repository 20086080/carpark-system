import unittest
from car_park import CarPark
from sensor import Sensor, EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = EntrySensor(1, CarPark("123 Example Street",
                                             100),True)
        self.exit_sensor = ExitSensor(2, CarPark("123 Example Street",
                                             100),True)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.entry_sensor.car_park.capacity, 100)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park.location, "123 Example Street")

    def test_exit_sensor_car_park_attributes(self):
        self.assertEqual(self.exit_sensor.car_park.capacity, 100)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.car_park.location, "123 Example Street")
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_entry_sensor_part_of_sensor(self):
        self.assertIsInstance(self.entry_sensor, Sensor)

    def test_exit_sensor_part_of_sensor(self):
        self.assertIsInstance(self.exit_sensor, Sensor)