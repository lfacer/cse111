import math

items = float(input("Enter the number of items: "))
boxes = float(input("Enter the number of items per box: "))

total = float
total = math.ceil(items/boxes)

print(f"For {items:.0f} items, packing {boxes:.0f} items in each box, you will need {total} boxes.")
