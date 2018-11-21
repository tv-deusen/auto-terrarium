import argparse
import time
import subprocess

from .Exceptions import CompileException
from multiprocessing import Process
from pathlib import Path
from dht import DHTDriver, common


sensor_types = ('DHT11', 'DHT22', 'AM2302')
# Adafruit code converts str to int for use in driver code
sensor_mapping = {'DHT11': common.DHT11,
                  'DHT22': common.DHT22,
                  'AM2302': common.AM2302}


def parse_args():
    parser = argparse.ArgumentParser(description="run AM2302 sensor reading")
    parser.add_argument('sensor', type=str)
    parser.add_argument('pin', type=int)
    parser.add_argument('database_path', type=str)
    return parser.parse_args()


def compile_dht_library():
    makecmd = "make shared"
    proc = subprocess.Popen(makecmd.split(), cwd="./dht/", stdout=subprocess.PIPE)
    _, err = proc.communicate()
    if err is not None:
        raise CompileException("failed to compile DHT C driver code")


def start_read(sensor, pin):
    driver = DHTDriver(sensor, pin)
    while 1:
        driver.get_reading()
        time.sleep(5)


def main():
    args = parse_args()
    sensor = args.sensor.upper()
    pin = args.pin
    db_path = Path(args.database_path)

    try:
        compile_dht_library()
    except CompileException as e:
        print(e.msg)
        exit(1)

    assert sensor in sensor_types, "Invalid sensor type '{}'".format(sensor)
    assert pin > 1

    p = Process(target=start_read, args=(sensor_mapping.get(sensor), pin))
    p.start()
    p.join()  # just block for now


if __name__ == "__main__":
    main()
