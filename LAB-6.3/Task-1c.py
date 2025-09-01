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


# Get input from user
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

# Create student object and display details
student1 = Student(name, roll_no, marks)
student1.display()
print(f"Grade: {student1.grade()}")
