#Write a program to take the temperatures of all 7 days of the week and displays the average temperature of that week.
temperatures = []
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    temp = float(input(f"Enter the temperature for {day}: "))
    temperatures.append(temp)
average_temp = sum(temperatures) / len(temperatures)
print(f"The average temperature for the week is: {average_temp:.2f}°C")