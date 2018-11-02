typedef struct reading_t {
    int read_result;
    float humidity;
    float temperature;
} Reading;

Reading d_read(int sensor, int pin);