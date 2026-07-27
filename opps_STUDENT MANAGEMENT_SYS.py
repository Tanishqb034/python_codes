class Student:

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print("---------------------------")
        print("ID   :", self.student_id)
        print("Name :", self.name)
        print("Age  :", self.age)


class StudentManagement:

    def __init__(self):
        self.students = []

    def add_student(self):

        student_id = input("Enter ID : ")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))

        student = Student(student_id, name, age)

        self.students.append(student)

        print("\nStudent Added Successfully.")

    def view_students(self):

        if len(self.students) == 0:
            print("\nNo Student Found")
            return

        print("\nStudent List\n")

        for student in self.students:
            student.display()

    def search_student(self):

        sid = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == sid:
                print("\nStudent Found")
                student.display()
                return

        print("\nStudent Not Found")

    def delete_student(self):

        sid = input("Enter Student ID : ")

        for student in self.students:

            if student.student_id == sid:
                self.students.remove(student)
                print("\nStudent Deleted Successfully.")
                return

        print("\nStudent Not Found")


system = StudentManagement()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.view_students()

    elif choice == "3":
        system.search_student()

    elif choice == "4":
        system.delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")