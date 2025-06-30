class Student:
    def __init__(self, name, age, depart, grade, contact):
        self.name = name
        self.age = age
        self.depart = depart
        self.grade = grade
        self.contact = contact

    def show(self):
        print('Name:', self.name, 'Age:', self.age, 'Department:', self.depart,
              'Grade:', self.grade, 'Contact:', self.contact)

    def adding(self,name,age,depart,grade,contact):
      self.name = name
      self.age = age
      self.depart = depart
      self.grade = grade
      self.contact = contact

    def calculate_average_of_grades(student_list):
        total = 0
        for s in student_list:
            total += s.grade
        average = total / len(student_list)
        print("Average Grade of Students is:", round(average, 2))

    def get_top_students(student_list):
        highest = max(s.grade for s in student_list)
        print("Highest Grade is:", highest)
        print("Student(s) with the highest grade:")
        for s in student_list:
            if s.grade == highest:
                s.show()

students = []

# command-line interface
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Calculate Average Grade")
    print("4. Show Top Student(s)")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        depart = input("Enter department: ")
        grade = float(input("Enter grade: "))
        contact = input("Enter contact: ")
        students.append(Student(name, age, depart, grade, contact))
        print("Student added successfully.")

    elif choice == "2":
        if students:
            for s in students:
                s.show()
        else:
            print("No students to display.")

    elif choice == "3":
        if students:
            Student.calculate_average_of_grades(students)
        else:
            print("No students available to calculate average.")

    elif choice == "4":
        if students:
            Student.get_top_students(students)
        else:
            print("No students available to evaluate.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")