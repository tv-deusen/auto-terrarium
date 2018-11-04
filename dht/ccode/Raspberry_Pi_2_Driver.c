#include <stdlib.h>
#include <stdio.h>
#include "Raspberry_Pi_2_Driver.h"
#include "Raspberry_Pi_2/pi_2_dht_read.h"

// Needed to free the struct from the Python wrapper
void free_read_result(Reading *r)
{
    free(r);
}

Reading* d_read(int sensor, int pin)
{
    float humidity = 0, temperature = 0;
    Reading *result = malloc(sizeof(Reading));
    int res = pi_2_dht_read(sensor, pin, &humidity, &temperature);
    result->read_result = res;
    result->humidity = humidity;
    result->temperature = temperature;
    return result;
}
