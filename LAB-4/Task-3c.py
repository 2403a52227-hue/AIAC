def extract_student_details(student_dict):
    """
    Extract student details from a nested dictionary.
    Args:
        student_dict (dict): Nested dictionary containing student information
    Returns:
        dict: Dictionary containing full name, branch, and SGPA
        or None if required fields are missing
    """
    try:
        # Extract full name (combining first and last name)
        first_name = student_dict.get('personal_info', {}).get('first_name', '')
        last_name = student_dict.get('personal_info', {}).get('last_name', '')
        full_name = f"{first_name} {last_name}".strip()
        # Extract branch
        branch = student_dict.get('academic_info', {}).get('branch', '')
        # Extract SGPA
        sgpa = student_dict.get('academic_info', {}).get('sgpa', '')
        # Check if all required fields are present
        if full_name and branch and sgpa != '':
            return {
                'full_name': full_name,
                'branch': branch,
                'sgpa': sgpa}
        else:
            return None
    except (KeyError, TypeError, AttributeError):
        return None
if __name__ == "__main__":
    # Sample student data
    student1 = {
        'personal_info': {
            'first_name': 'Jaya',
            'last_name': 'Surya',
            'age': 20,
            'email': 'surya.@email.com'},
        'academic_info': {
            'branch': 'Computer Science',
            'sgpa': 8.5,
            'semester': 4,
            'courses': ['Python', 'Data Structures', 'Algorithms']}}
    student2 = {
        'personal_info': {
            'first_name': 'Eshwar',
            'last_name': 'charan',
            'age': 19
        },
        'academic_info': {
            'branch': 'Electrical Engineering',
            'sgpa': 9.2,
            'semester': 3,
            'courses': ['Java','Computer networks']}}
    student3 = {
        'personal_info': {
            'first_name': 'Teja',
            'age': 19
        },
        'academic_info': {
            'branch': 'Mechanical Engineering',
            'sgpa': 9.3,
            'semester': 4,
            'courses': ['Web technology','Physics']   }}
    # Test the function
    print("Student Details Extractor")
    print("=" * 30)
    # Test with complete data
    result1 = extract_student_details(student1)
    print(f"Student 1: {result1}")
    result2 = extract_student_details(student2)
    print(f"Student 2: {result2}")
    # Test with incomplete data
    result3 = extract_student_details(student3)
    print(f"Student 3: {result3}")
    # Test with empty dictionary
    result4 = extract_student_details({})
    print(f"Empty dict: {result4}")
    # Test with None
    result5 = extract_student_details(None)
    print(f"None input: {result5}")
