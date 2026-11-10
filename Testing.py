import time

def attack(delay, damage, strikes = 10):
    for i in range(strikes):
            print(f"Ow! (-{damage})")
            time.sleep(delay)

PD = float(input("How quickly? "))
DMG = int(input("How much damage? "))
TRK = int(input("How many strikes? "))

BRT = int(input("How many bursts? "))
y = 1

while y <= BRT:
    attack(PD, DMG, TRK)
    y += 1
    time.sleep(1)