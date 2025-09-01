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
# Initialize counter
student_count = 1
# Process students using while loop
while True:
    print(f"\n--- Student {student_count} ---")
    # Get student details from user
    name = input("Enter student name (or 'quit' to exit): ")
    # Check for exit condition
    if name.lower() == 'quit':
        print("Exiting program...")
        break
    roll_no = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    # Create student object and display details
    student = Student(name, roll_no, marks)
    student.display()
    print(f"Grade: {student.grade()}")
    print("-" * 30)
    
    # Increment counter
    student_count += 1
