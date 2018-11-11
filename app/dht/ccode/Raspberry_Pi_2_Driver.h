typedef struct reading_t {
    int read_result;
    float humidity;
    float temperature;
} Reading;

void free_read_result(Reading *r);
Reading* d_read(int sensor, int pin);