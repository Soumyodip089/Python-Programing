#Write a python program that asks your height in centimeters and converts it into foot and inches
def cm_to_feet_inches(cm):
    inches = cm / 2.54
    feet = int(inches // 12)
    inches = round(inches % 12)
    return feet, inches

cm = float(input("Enter your height in centimeters: "))
feet, inches = cm_to_feet_inches(cm)
print(f"Your height is {feet} feet and {inches} inches.")
