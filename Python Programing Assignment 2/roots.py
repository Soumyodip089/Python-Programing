#Write a program to calculate the roots of a given quadratic equation
import cmath
def calculate(a,b,c):
    discr=b**2-4*a*c
    root1=(-b+cmath.sqrt(discr))/(2*a)
    root2=(-b-cmath.sqrt(discr))/(2*a)
    return root1,root2
a=int(input("Enter coefficient of a:"))
b=int(input("Enter coefficient of b:"))
c=int(input("Enter coefficient of c:"))
root1,root2=calculate(a,b,c)
print(f"Two roots of the quadratic Equation are {root1} and {root2}")