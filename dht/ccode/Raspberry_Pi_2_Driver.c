#include "Raspberry_Pi_2_Driver.h"
#include "Raspberry_Pi_2/pi_2_dht_read.h"


Reading d_read(int sensor, int pin)
{
    float humidity = 0, temperature = 0;
    Reading result;
    int res = pi_2_dht_read(sensor, pin, &humidity, &temperature);
    result.read_result = res;
    result.humidity = humidity;
    result.temperature = temperature;
    return result;
}