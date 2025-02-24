#7.Write a python program to enter names of employees and their salaries as input and store them in a dictionary (Take input multiple times based on user choice).

employee_data = {}

def add_employee():
    name = input("Enter employee's name: ")
    salary = float(input("Enter employee's salary: "))
    employee_data[name] = salary
    print(f"Employee '{name}' added successfully!")

def display_employees():
    if not employee_data:
        print("No employees added yet!")
    else:
        print("Employee Data:")
        for name, salary in employee_data.items():
            print(f"{name}: Rs{salary:.2f}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            display_employees()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
