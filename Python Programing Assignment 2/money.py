#Write a program to convert dollars in Rupee
conversion_rate = 87.48
dollars = float(input("Enter the amount in dollars: "))
rupees = dollars * conversion_rate
print(f"${dollars} is equal to ₹{rupees:.2f}")