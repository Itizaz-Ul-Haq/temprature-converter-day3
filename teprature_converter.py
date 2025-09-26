# ........Define functions for both Calsius and Fahrenheit.....

def Celsius_to_Fahrenheit(celsius):
    return (Celsius*9/5)+32


def Fahrenheit_to_Celsius(Fahreheit):
    return (Fahreheit-32)*5/9

# .......Taking inputs from user.................


choice = input("what you want to convert : F to C ? or C to F?: ").lower()

# .......Use of conditional statements...........

if choice == "f to c":
    Fahrenheit = int(input("Enter the value in fahrenheit: "))
    print(f"{Fahrenheit} fahrenheits are equals to {Fahrenheit_to_Celsius(Fahrenheit)} Celcius ")

elif choice == "c to f":
    Celsius = int(input("Enter the value in celsius: "))
    print(f"{Celsius} Celsius is equals to {Celsius_to_Fahrenheit(Celsius)} Fahrenheits")
