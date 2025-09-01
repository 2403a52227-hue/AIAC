def classify_age(age):
    if age < 2:
        return "Infant"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teen"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
# Initialize variables
ages = []
age_count = 1
# Get ages from user using while loop
while True:
    age_input = input(f"Enter age {age_count} (or 'done' to finish): ")
    # Check for exit condition
    if age_input.lower() == 'done':
        break
    try:
        age = int(age_input)
        ages.append(age)
        age_count += 1
    except ValueError:
        print("Please enter a valid number or 'done'")
print("\nAge Classification Results:")
print("-" * 40)
# Classify each age using while loop
i = 0
while i < len(ages):
    age = ages[i]
    category = classify_age(age)
    print(f"Age {i+1}: {age} years old - {category}")
    i += 1
print("-" * 40)
