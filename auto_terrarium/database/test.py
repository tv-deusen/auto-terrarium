import os
import unittest
from datetime import datetime, date
from pathlib import Path

# from auto_terrarium_proj.Reading import Reading
from .ReadingsDB import ReadingsDBController, DEFAULT_DB_FILE
from web_monitor.models import Reading

curtime = datetime.now()
test_reading = Reading(curtime, 72, 44)


class TestReadingsDB(unittest.TestCase):

    def setUp(self):
        path = Path(DEFAULT_DB_FILE)
        if Path.exists(path):
            os.remove(DEFAULT_DB_FILE)

    def test_get_latest_reading(self):
        ReadingsDBController.create_readings_table('test.sqlite', reinit=True)
        db = ReadingsDBController('test.sqlite')

        db.write(test_reading)
        reading = db.get_latest_reading()

        self.assertEqual(reading.time, test_reading.time)
        self.assertEqual(reading.temperature, test_reading.temperature)
        self.assertEqual(reading.humidity, test_reading.humidity)

        ReadingsDBController.drop_readings_table('test.sqlite')

    def test_record_good_reading(self):
        ReadingsDBController.create_readings_table('test.sqlite', reinit=True)
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
