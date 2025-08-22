class SRU_Student:
    """Represents a student with basic details and provides a method
    to persist those details to a text document.

    Attributes:
        name (str): Student name
        roll_no (str): Roll number (kept as string to preserve formatting like leading zeros)
        department (str): Department name
        batch (str): Batch identifier (e.g., "2021-2025" or "Batch-1")
        year (str): Current academic year or year of study
    """

    def __init__(self, name: str, roll_no: str, department: str, batch: str, year: str) -> None:
        self.name = name.strip()
        self.roll_no = roll_no.strip()
        self.department = department.strip()
        self.batch = batch.strip()
        self.year = year.strip()

    def __str__(self) -> str:
        return (
            f"Name: {self.name} | Roll No: {self.roll_no} | Department: {self.department}"
            f" | Batch: {self.batch} | Year: {self.year}"
        )

    def student_data(self, file_path: str = "student_details.txt") -> str:
        """Append this student's details to a text file.

        Args:
            file_path: Destination text file. Defaults to 'student_details.txt' in the current folder.

        Returns:
            The path of the file where the data was written.
        """
        record = (
            "==============================\n"
            f"Name       : {self.name}\n"
            f"Roll No    : {self.roll_no}\n"
            f"Department : {self.department}\n"
            f"Batch      : {self.batch}\n"
            f"Year       : {self.year}\n"
            "==============================\n\n"
        )

        # Append so multiple students can be recorded in the same document
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(record)

        # Also append to an additional text file named 'student-details.txt'
        alt_path = "student-details.txt"
        with open(alt_path, "a", encoding="utf-8") as f2:
            f2.write(record)

        return file_path


def _input_non_empty(prompt: str) -> str:
    """Prompt until the user enters a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


if __name__ == "__main__":
    print("Enter SRU Student Details")
    name = _input_non_empty("Name        : ")
    roll_no = _input_non_empty("Roll No     : ")
    department = _input_non_empty("Department  : ")
    batch = _input_non_empty("Batch       : ")
    year = _input_non_empty("Year        : ")

    student = SRU_Student(name=name, roll_no=roll_no, department=department, batch=batch, year=year)
    saved_to = student.student_data()  # writes to 'student_details.txt' by default

    print("\nSaved student details:")
    print(student)
    print(f"\nDetails appended to: {saved_to}")


