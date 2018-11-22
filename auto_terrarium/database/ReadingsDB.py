import sqlite3
from pathlib import Path

from auto_terrarium.Exceptions import *
# from auto_terrarium_app.Reading import Reading
from main_site.models import Reading

# ReadingsDB Requirements:
# - Initialization
# - Deletion (or at least freeing space)
# - Multiprocess connection (need to figure how)
# - Insertion
# - Reading

DEFAULT_DB_FILE = "readings.sqlite"


class ReadingsDBController:

    def __init__(self, db_path=DEFAULT_DB_FILE, expiry=30):
        self._DB_PATH_ = db_path
        db_file = Path(self._DB_PATH_)
        if not Path.exists(db_file):
            self.create_readings_table()

        # PARSE_DECLTYPES: makes module parse the declared type for each column it returns
        # PARSE_COLNAMES: makes module parse column name for each column it returns
        self._connection = sqlite3.connect(self._DB_PATH_,
                                           detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self._expiry = expiry

    # I feel like using _DB_FILE_ in this way in the static methods below is a bad idea...
    @staticmethod
    def create_readings_table(db_path=DEFAULT_DB_FILE, reinit=False):
        path = Path(db_path)
        if Path.exists(path) and not reinit:
            raise DBCreateException("{} already exists".format(db_path))

        new_connection = sqlite3.connect(db_path)
        cursor = new_connection.cursor()

        cursor.execute('''CREATE TABLE readings
                            (id INTEGER PRIMARY KEY, time TIMESTAMP, temp REAL, humidity REAL)''')
        new_connection.commit()
        new_connection.close()

        if not Path.exists(path):
            raise DBCreateException("Could not create database at {}".format(db_path))

    @staticmethod
    def drop_readings_table(db_path=DEFAULT_DB_FILE):
        path = Path(db_path)
        if not Path.exists(path):
            raise DBDropException("{} does not exist".format(db_path))

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''DROP TABLE readings''')
        conn.commit()
        conn.close()


    def get_connection(self):
        return self._connection


    # Readings from the sensor are only being taken once every
    # five minutes, so getting the latest one should be acceptable for display
    def get_latest_reading(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM readings ORDER BY time DESC LIMIT 1")
        # can we iterate over the query?
        # query = cursor.fetchone()
        _, time, temp, hum = cursor.fetchone()

        if hum < 0 or hum > 100:
            raise BadQueryException("Invalid humidity from query: {}".format(hum))

        # only check for absurd values right now
        if temp < -100 or temp > 130:
            raise BadQueryException("Absurd temperature from query: {}".format(temp))

        return Reading(time, temp, hum)

    def write(self, reading):
        cursor = self._connection.cursor()

        if reading.humidity > 100 or reading.humidity < 0:
            raise BadInsertException("Humidity value doesn't make sense: {}".format(reading.humidity))

        if reading.temperature < -100 or reading.temperature > 130:
            raise BadInsertException("Temp is too extreme: {}, I'm in danger".format(reading.temperature))

        cursor.execute('''INSERT INTO readings(time, temp, humidity) VALUES(?,?,?)''',
                       (reading.time, reading.temperature, reading.humidity))

        self._connection.commit()
