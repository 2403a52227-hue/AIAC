class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
    
    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'


# Get number of students from user
num_students = int(input("Enter number of students: "))

# Process students using for loop with user input
for i in range(num_students):
    print(f"\n--- Student {i+1} ---")
    
    # Get student details from user
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    
    # Create student object and display details
    student = Student(name, roll_no, marks)
    student.display()
    print(f"Grade: {student.grade()}")
    print("-" * 30)
