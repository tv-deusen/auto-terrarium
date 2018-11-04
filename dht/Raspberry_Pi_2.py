# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
# import Raspberry_Pi_2_Driver as driver
from ctypes import c_int, c_float, c_void_p, Structure, CDLL

from . import common


class Reading(Structure):
    _fields_ = [('result', c_int),
                ('humidity', c_float),
                ('temperature', c_float)]


def load_dll(path):
    '''
    Compiles C driver code if necessary into ./dht/ccode/dht.so and
    creates a ctypes CDLL object with the correct argtypes and argres set.
    :param path: str path to the shared library file
    :return: CDLL object of DHT driver code
    '''
    driver = CDLL(path)
    driver.d_read.argtypes = [c_int]
    driver.d_read.restype = c_void_p
    return driver

def read(sensor, pin):
    '''
    Bit of a convoluted wrapper to perform the reading of the sensor specified.
    :param sensor:
    :param pin:
    :return: A tuple of floats containing the humidity and temperature readings respectively
    '''

    shared_lib_path = os.getcwd() + '/dht/ccode/dht.so'

    driver = load_dll(shared_lib_path)

    # Validate pin is a valid GPIO.
    if pin is None or int(pin) < 0 or int(pin) > 31:
        raise ValueError('Pin must be a valid GPIO number 0 to 31.')

    # Get a reading from C driver code.
    reading_ptr = driver.d_read(sensor, pin)

    reading = Reading.from_address(reading_ptr)
    result = reading.result
    humidity = reading.humidity
    temperature = reading.temperature * 9 / 5.0 + 32

    if result in common.TRANSIENT_ERRORS:
        # Signal no result could be obtained, but the caller can retry.
        return (None, None)
    elif result == common.DHT_ERROR_GPIO:
        raise RuntimeError('Error accessing GPIO.')
    elif result != common.DHT_SUCCESS:
        # Some kind of error occured.
        raise RuntimeError('Error calling DHT test driver read: {0}'.format(result))

    driver.free_read_result(reading_ptr)
    return humidity, temperature
