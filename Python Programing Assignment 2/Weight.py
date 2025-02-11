#Write a program to calculate body mass index of a person. BMI=kg/m^2 where kg is a person's weight in kilogram and m^2 is the height in meter squared
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = weight_kg / (height_m ** 2)
print(f"Your BMI is: {bmi:.2f}")