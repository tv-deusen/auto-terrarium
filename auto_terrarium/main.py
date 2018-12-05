import argparse
import subprocess
import time
from multiprocessing import Process
from pathlib import Path

from dht import DHTDriver, common

from .Exceptions import CompileException
from .monitor import Monitor

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
    make_cmd = "make shared"
    proc = subprocess.Popen(make_cmd.split(), cwd="./dht/", stdout=subprocess.PIPE)
    _, err = proc.communicate()
    if err is not None:
        raise CompileException("failed to compile DHT C driver code")


def start_drivers(sensor, pin, best_temp, best_hum):
    dht = DHTDriver(sensor, pin)
    mntr = Monitor(best_temp, best_hum)



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

    # Start DHT reading and monitor
    # Make it a signal handler for server too?

    p = Process(target=start_drivers, args=(sensor_mapping.get(sensor), pin))
    p.start()
    p.join()  # just block for now


if __name__ == "__main__":
    main()
