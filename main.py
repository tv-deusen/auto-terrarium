
from dht import AM2302
from dht import DHTDriver

def main():
    driver = DHTDriver(AM2302, 4)
    driver.get_reading()

if __name__ == "__main__":
    main()