#9.Write a Python program to read marks of six subjects and to print the marks scored in each subject and show the total marks. Print the highest and lowest marks.

subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))
subject6 = float(input("Enter marks of Subject 6: "))

print("\nMarks Scored in Each Subject:")
print(f"Subject 1: {subject1}")
print(f"Subject 2: {subject2}")
print(f"Subject 3: {subject3}")
print(f"Subject 4: {subject4}")
print(f"Subject 5: {subject5}")
print(f"Subject 6: {subject6}")

total_marks = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
print(f"\nTotal Marks: {total_marks}")

highest_marks = max(subject1, subject2, subject3, subject4, subject5, subject6)
print(f"Highest Marks: {highest_marks}")

lowest_marks = min(subject1, subject2, subject3, subject4, subject5, subject6)
print(f"Lowest Marks: {lowest_marks}")
