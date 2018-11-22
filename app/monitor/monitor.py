class Monitor:
    """
    Monitors the latest temperature and humidity readings
    Keeps various stats I guess to consider triggering various regulators
    Regulator requirements TBD
    """

    def __init__(self, temp, humididty):
        self.optimum_temp = temp
        self.optimum_humidity = humididty
        self.average_temp = temp
        self.average_hum = humididty

    def check_latest_reading(self):
        """

        :return:
        """
