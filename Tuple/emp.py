
import numpy as np

# ==========================================
# EMPLOYEE MANAGEMENT SYSTEM
# Python + NumPy
# ==========================================

# Columns:
# ID | Name | Department | Salary

employees = np.array([
    [101, "Rahul", "IT", 45000],
    [102, "Priya", "HR", 35000],
    [103, "Aman", "IT", 55000],
    [104, "Neha", "Sales", 40000],
    [105, "Rohit", "Finance", 60000]
], dtype=object)


# ==========================================
# 1. DISPLAY ALL EMPLOYEES
# ==========================================

def display_employees():

    print("\n========== EMPLOYEE LIST ==========")

    if len(employees) == 0:
        print("No employees found.")
        return

    print("ID\tName\tDepartment\tSalary")
    print("-" * 45)

    for employee in employees:
        print(
            employee[0],
            "\t",
            employee[1],
            "\t",
            employee[2],
            "\t\t",
            employee[3]
        )


# ==========================================
# 2. ADD EMPLOYEE
# ==========================================

def add_employee():

    global employees

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    new_employee = np.array(
        [[emp_id, name, department, salary]],
        dtype=object
    )

    employees = np.vstack((employees, new_employee))

    print("\nEmployee added successfully!")


# ==========================================
# 3. SEARCH EMPLOYEE
# ==========================================

def search_employee():

    emp_id = int(input("Enter Employee ID: "))

    result = employees[employees[:, 0] == emp_id]

    if len(result) == 0:
        print("Employee not found.")

    else:
        print("\nEmployee Found:")
        print("ID:", result[0, 0])
        print("Name:", result[0, 1])
        print("Department:", result[0, 2])
        print("Salary:", result[0, 3])


# ==========================================
# 4. UPDATE SALARY
# ==========================================

def update_salary():

    global employees

    emp_id = int(input("Enter Employee ID: "))
    new_salary = int(input("Enter New Salary: "))

    mask = employees[:, 0] == emp_id

    if np.sum(mask) == 0:
        print("Employee not found.")

    else:
        employees[mask, 3] = new_salary

        print("Salary updated successfully!")


# ==========================================
# 5. DELETE EMPLOYEE
# ==========================================

def delete_employee():

    global employees

    emp_id = int(input("Enter Employee ID: "))

    mask = employees[:, 0] != emp_id

    if np.sum(mask) == len(employees):
        print("Employee not found.")

    else:
        employees = employees[mask]

        print("Employee deleted successfully!")


# ==========================================
# 6. HIGHEST SALARY
# ==========================================

def highest_salary():

    salary = employees[:, 3].astype(int)

    index = np.argmax(salary)

    print("\nHighest Paid Employee")
    print("---------------------")

    print("ID:", employees[index, 0])
    print("Name:", employees[index, 1])
    print("Department:", employees[index, 2])
    print("Salary:", employees[index, 3])


# ==========================================
# 7. AVERAGE SALARY
# ==========================================

def average_salary():

    salary = employees[:, 3].astype(int)

    print("\nAverage Salary:", np.mean(salary))


# ==========================================
# 8. DEPARTMENT SEARCH
# ==========================================

def department_search():

    department = input("Enter Department: ")

    result = employees[
        employees[:, 2] == department
    ]

    if len(result) == 0:
        print("No employees found.")

    else:

        print("\nEmployees in", department)

        print("ID\tName\tSalary")
        print("-" * 30)

        for employee in result:
            print(
                employee[0],
                "\t",
                employee[1],
                "\t",
                employee[3]
            )


# ==========================================
# 9. SALARY FILTER
# ==========================================

def salary_filter():

    amount = int(
        input("Enter minimum salary: ")
    )

    salary = employees[:, 3].astype(int)

    result = employees[salary >= amount]

    if len(result) == 0:
        print("No employees found.")

    else:

        print("\nEmployees earning >=", amount)

        print("ID\tName\tSalary")
        print("-" * 30)

        for employee in result:
            print(
                employee[0],
                "\t",
                employee[1],
                "\t",
                employee[3]
            )


# ==========================================
# 10. SORT BY SALARY
# ==========================================

def sort_by_salary():

    salary = employees[:, 3].astype(int)

    index = np.argsort(salary)[::-1]

    sorted_employees = employees[index]

    print("\nEmployees Sorted By Salary")
    print("--------------------------")

    print("ID\tName\tSalary")

    for employee in sorted_employees:

        print(
            employee[0],
            "\t",
            employee[1],
            "\t",
            employee[3]
        )


# ==========================================
# 11. EMPLOYEE COUNT
# ==========================================

def employee_count():

    print(
        "\nTotal Employees:",
        len(employees)
    )


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("===================================")
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Display Employees")
    print("2. Add Employee")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Highest Salary")
    print("7. Average Salary")
    print("8. Search By Department")
    print("9. Salary Filter")
    print("10. Sort By Salary")
    print("11. Employee Count")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_employees()

    elif choice == "2":
        add_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        highest_salary()

    elif choice == "7":
        average_salary()

    elif choice == "8":
        department_search()

    elif choice == "9":
        salary_filter()

    elif choice == "10":
        sort_by_salary()

    elif choice == "11":
        employee_count()

    elif choice == "12":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

