problem: calculating the pool area and the tiles needed to make a circular pool

import math

print ("hello to the pool engineer")
radius = float(input("what is the radius of the pool? "))

area = 3.14*(pow(radius,2))

print(f"the area of the pool is {area:.2f} m^2")
print(f"you will need {math.ceil(area)} tiles")
