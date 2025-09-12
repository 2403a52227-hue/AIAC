# Define the sru_student class
class sru_student:
    # Initialize the attributes: name, roll no., hostel_status
    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Student's name
        self.roll_no = roll_no  # Student's roll number
        self.hostel_status = hostel_status  # Hostel status (e.g., 'Yes' or 'No')
        self.fee_paid = False  # Track if fee is paid

    # Method to update fee status
    def fee_update(self, status):
        self.fee_paid = status  # Update fee status (True for paid, False for not paid)

    # Method to display student details
    def display_details(self):
        print("Name:", self.name)  # Print student's name
        print("Roll No.:", self.roll_no)  # Print student's roll number
        print("Hostel Status:", self.hostel_status)  # Print hostel status
        print("Fee Paid:", "Yes" if self.fee_paid else "No")  # Print fee status

# Take input from user to create a new student
name = input("Enter student's name: ")  # Prompt user for student's name
roll_no = input("Enter student's roll number: ")  # Prompt user for roll number
hostel_status = input("Is the student staying in hostel? (Yes/No): ")  # Prompt for hostel status
fee_paid_input = input("Has the fee been paid? (Yes/No): ")  # Prompt for fee payment status

# Convert fee_paid_input to boolean
fee_paid = True if fee_paid_input.strip().lower() == "yes" else False  # Convert input to boolean

# Create a new student object with user input
student = sru_student(name, roll_no, hostel_status)  # Create student object with user input
student.fee_update(fee_paid)  # Update fee status based on user input
student.display_details()  # Display details of student