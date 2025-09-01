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
# Get number of ages from user
num_ages = int(input("Enter number of ages to classify: "))
# Get ages from user
ages = []
for i in range(num_ages):
    age = int(input(f"Enter age {i+1}: "))
    ages.append(age)
print("\nAge Classification Results:")
print("-" * 40)
# Classify each age using for loop
for i, age in enumerate(ages, 1):
    category = classify_age(age)
    print(f"Age {i}: {age} years old - {category}")
print("-" * 40)
