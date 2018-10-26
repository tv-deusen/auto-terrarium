CC = gcc
CFLAGS = -g -Wall -O0 -IRaspberry_Pi -IRaspberry_Pi_2

debug: debug.o
	$(CC) $(CFLAGS) -o debug debug.o

debug.o:	 Raspberry_Pi/pi_mmio.h Raspberry_Pi_2/pi_2_mmio.h Raspberry_Pi/pi_mmio.c Raspberry_Pi/pi_dht_read.c Raspberry_Pi_2/pi_2_mmio.c Raspberry_Pi_2/pi_2_dht_read.c Test/debug.c
	$(CC) $(CFLAGS) -c debug.o Raspberry_Pi/pi_mmio.c Raspberry_Pi/pi_dht_read.c Raspberry_Pi_2/pi_2_mmio.c Raspberry_Pi_2/pi_2_dht_read.c Test/debug.c

# # read.o:	Raspberry_Pi/pi_mmio.c Raspberry_Pi/pi_dht_read.c Raspberry_Pi_2/pi_2_mmio.c Raspberry_Pi_2/pi_2_dht_read.c
# # 	$(CC) $(CFLAGS) Raspberry_Pi/pi_mmio.c Raspberry_Pi/pi_dht_read.c Raspberry_Pi_2/pi_2_mmio.c Raspberry_Pi_2/pi_2_dht_read.c
