# Ohm's Law

from src import Law

ask = True

while ask:
    print("--------------------------")
    print("--------Ohm's law---------")
    print("1. Calculate Voltage")
    print("2. Calculate Resistance")
    print("3. Calculate Current")
    print("--------------------------")
    ask = input("Choose An Option (1-3): ")
    if (ask == 1):
        print ("-- Calculating Voltage --")
        i = float(input("   Enter the current: "))
        r = float(input("   Enter the resistence: "))
        break