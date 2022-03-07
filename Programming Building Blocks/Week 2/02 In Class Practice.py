import math

def compute_circle_area(radius):
    return radius**2 * math.pi
    
radius =  float(input("Please enter a radius: "))

print(round(compute_circle_area(radius),2))
#another way to round is 
#area = round(area,2)

x = ["cse111", "cse280", "cs165"]
for i in x:
    print(i, i, i, sep="\n")