import argparse
import time
from multiprocessing import Process

from dht import DHTDriver
from dht import SENSORS

sensor_types = ('dht11', 'dht22', 'am2302')


def parse_args():
    parser = argparse.ArgumentParser(description="run AM2302 sensor reading")
    parser.add_argument('sensor', type=int)
    parser.add_argument('pin', type=int)
    return parser.parse_args()


def start_read(sensor, pin):
    while 1:
        driver = DHTDriver(sensor, pin)
        driver.get_reading()
        time.sleep(5)

def main():
    args = parse_args()
    sensor = args.sensor
    pin = args.pin

    assert sensor in SENSORS, "Invalid sensor type '{}'".format(sensor)
    assert pin > 1

    p = Process(target=start_read, args=(sensor, pin))
    p.start()
    p.join()  # just block for now

if __name__ == "__main__":
    main()
