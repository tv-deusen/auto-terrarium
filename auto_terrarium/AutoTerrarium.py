import time
from .dht import DHTDriver


class AutoTerrarium:

    def __init__(self, optimums, sensor_type='AM2302', pin=4):
        """

        :param optimums:
        :param sensor_type:
        :param pin:
        """
        self.dht = DHTDriver(sensor_type, pin)

    def start(self):
        while 1:
            humidity, temp = self.dht.get_reading()
            # TODO: how to handle regulating things?
            # mntr.check(humidity, temp)

            time.sleep(5)
