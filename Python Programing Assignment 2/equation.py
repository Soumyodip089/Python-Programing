#Write a program to take value of x,y,z from the user and calculate the equation
import math
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))
val=4*pow(x,4)+3*pow(y,3)+9*pow(z,2)+6*math.pi
print(f"Result={val:.2f}")