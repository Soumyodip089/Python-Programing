#Write a python program to print the area of circle when radius of the circle is given by user
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print("The area of the circle with radius", radius, "is", round(area, 2))
