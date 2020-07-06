# Ohm's Law Program 

from src import Law

ask = True

while ask:
    print("\n--------------------------")
    print("--------Ohm's law---------")
    print("1. Calculate Voltage")
    print("2. Calculate Resistance")
    print("3. Calculate Current")
    print("4. Exit Program")
    print("--------------------------")
    ask = input("\nChoose An Option (1-3): ")
    if ask == "1":
        print ("-- Calculating Voltage --")
        i = float(input("Enter the current(In Amps (A)): "))
        r = float(input("Enter the resistence(In Ohms(Ω)): "))
        result = Law.voltage(i, r)
        print(i, "*", r, "=", result)
    elif ask == "2":
        print ("-- Calculating Resistance --")
        v = float(input("Enter the Voltage(In Volts (V)): "))
        i = float(input("Enter the current(In Amps (A)): "))
        result = Law.resistance(v, i)
        print(v, "/", i, "=", result)
    elif ask == "3":
        print ("-- Calculating Current --")
        v = float(input("Enter the Voltage(In Volts (V)): "))
        r = float(input("Enter the resistence(In Ohms(Ω)): "))
        result = Law.current(v, r)
        print(v, "/", r, "=", result)
    else:
        print("\n--- Thank you. See You Later! ---")
        break