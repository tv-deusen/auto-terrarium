#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "../common_dht_read.h"
#include "pi_dht_read.h"
#include "pi_2_dht_read.h"

#define RASPI_1 "r1"
#define RASPI_2 "r2"

typedef enum sensor_t {
    ST_DHT11,
    ST_DHT22,
    ST_AM2302
} sensor_type;

typedef enum platform_t {
    PT_BEAGLEBONE,
    PT_RPI_1,
    PT_RPI_2
} platform_type;

static void test_read(platform_type platform, const int sensor, const int pin)
{
    float humidity = 0;
    float temperature = 0;
    int result = 0;

    while (1) {
        result = pi_2_dht_read(sensor, pin, &humidity, &temperature);
        if (result) {
            fprintf(stderr, "ERROR: RECEIVED %d FROM pi_2_dht_read\n", result);
            exit(1);
        }
        printf("From read: \n>>temp: %0f\n>>humidity: %0f\n", temperature, humidity);
        sleep(2);
    }
}

int main(int argc, char **argv)
{
    if (argc != 3) {
        printf("Usage: ./debug platform sensor pin\n");
        printf("Debug usage: gdb debug, then run with r [args...]\n");
    }


    platform_type platform;

    const char *arg_platform = argv[1];
    const int sensor = atoi(argv[2]);
    const int pin = atoi(argv[3]);

    const int r1 = strcmp(arg_platform, RASPI_1);
    const int r2 = strcmp(arg_platform, RASPI_2);

    if (r1 == 0) {
        platform = PT_RPI_1;
    } else if (r2 == 0) {
        platform = PT_RPI_2;
    } else {
        fprintf(stderr, "Error: gave platform: %s which is not supported", arg_platform);
        exit(1);
    }

    test_read(platform, sensor, pin);
    return 0;
}