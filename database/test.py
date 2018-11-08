import os
import unittest
from datetime import datetime, date
from pathlib import Path

from .Reading import Reading
from .ReadingsDB import ReadingsDBController

curtime = datetime.now()
test_reading = Reading(curtime, 72, 44)


class TestReadingsDB(unittest.TestCase):

    def setUp(self):
        path = Path(ReadingsDBController._DB_FILE_)
        if Path.exists(path):
            os.remove(ReadingsDBController._DB_FILE_)

    def test_get_latest_reading(self):
        ReadingsDBController.create_readings_table()
        db = ReadingsDBController()

        db.write(test_reading)
        reading = db.get_latest_reading()

        self.assertEqual(reading.time, test_reading.time)
        self.assertEqual(reading.temperature, test_reading.temperature)
        self.assertEqual(reading.humidity, test_reading.humidity)

        ReadingsDBController.drop_readings_table()

    def test_record_good_reading(self):
        ReadingsDBController.create_readings_table()
        db = ReadingsDBController()

        db.write(test_reading)
        ReadingsDBController.drop_readings_table()


class TestReading(unittest.TestCase):

    def test_bad_time(self):
        self.skipTest("not implemented yet")
        never = date.max
        reading = Reading(never, 72, 44)
        self.assertIsNone(reading, "class Reading init accepted bad temp value")


if __name__ == "__main__":
    unittest.main()
