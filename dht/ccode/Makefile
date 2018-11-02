CC = gcc
CFLAGS = -Wall -g -O0 -IRaspberry_Pi -IRaspberry_Pi_2

shared: Raspberry_Pi_2_Driver.o pi_2_mmio.o pi_2_dht_read.o
	$(CC) -shared -o dht.so Raspberry_Pi_2_Driver.o pi_2_dht_read.o pi_2_mmio.o common_dht_read.o

driver.o: Raspberry_Pi_2_Driver.h Raspberry_Pi_2_Driver.c pi_2_dht_read.o
	$(CC) $(CFLAGS) -c Raspberry_Pi_2_Driver.c

debug: debug.o pi_2_mmio.o pi_2_dht_read.o 
	$(CC) $(CFLAGS) -o debug debug.o pi_2_dht_read.o common_dht_read.o pi_2_mmio.o

debug.o:	pi_2_mmio.o pi_2_dht_read.o Test/debug.c
	$(CC) $(CFLAGS) -c Test/debug.c

pi_2_dht_read.o:	common_dht_read.o pi_2_mmio.o Raspberry_Pi_2/pi_2_dht_read.h Raspberry_Pi_2/pi_2_dht_read.c
	$(CC) $(CFLAGS) -c Raspberry_Pi_2/pi_2_dht_read.c

common_dht_read.o:	common_dht_read.h common_dht_read.c
	$(CC) $(CFLAGS) -c common_dht_read.c

pi_2_mmio.o:	Raspberry_Pi_2/pi_2_mmio.h Raspberry_Pi_2/pi_2_mmio.c
	$(CC) $(CFLAGS) -c Raspberry_Pi_2/pi_2_mmio.c

clean:
	rm pi_2_mmio.o common_dht_read.o pi_2_dht_read.o debug.o debug
