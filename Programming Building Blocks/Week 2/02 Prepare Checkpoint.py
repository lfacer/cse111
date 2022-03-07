import math
from datetime import datetime
current_date_and_time = datetime.now()

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))
v = 0
v = (math.pi * (w**2) * a * (w * a + 2540 * d))/10000000000

print()
print(f"The approximate volume is {v:.2f} liters\n")
purchase = input("Would you like to purchase the tires today? ")

#without phone number
if purchase.upper() != "YES":   
    with open("volume.txt", "a") as volume_file:
        volume_file.write(f"{current_date_and_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}\n")

#with phone number
elif purchase.upper() == "YES":
    with open("volume.txt", "a") as volume_file:
        phone_number = input("Please enter your phone number")
        volume_file.write(f"{current_date_and_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}, {phone_number} \n")