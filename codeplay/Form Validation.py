import re
from datetime import datetime

# 1. Validate Full Name
def validate_name(name):
    pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
    return bool(re.fullmatch(pattern, name))

# 2. Validate Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, email))

# 3. Validate Phone Number
def validate_phone(phone):
    pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, phone))

# 4. Validate Password
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.fullmatch(pattern, password))

# 5. Validate Age
def validate_age(age):
    if not age.isdigit():
        return False
    age = int(age)
    return 10 <= age <= 99

# 6. Validate Username
def validate_username(username):
    pattern = r'^[a-zA-Z0-9]{5,15}$'
    return bool(re.fullmatch(pattern, username))

# 7. Validate Date of Birth using datetime
def validate_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# 8. Validate Address
def validate_address(address):
    return len(address.strip()) >= 10

# Function to repeatedly ask until valid
def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def main():
    print("\nFORM VALIDATION PROGRAM USING REGULAR EXPRESSIONS\n")

    name = get_valid_input("Enter your full name (e.g., John Doe): ", validate_name)
    email = get_valid_input("Enter your email: ", validate_email)
    phone = get_valid_input("Enter your phone number: ", validate_phone)
    username = get_valid_input("Create a username (5-15 alphanumeric characters): ", validate_username)
    password = get_valid_input("Create a password (min 8 chars, 1 uppercase, 1 number, 1 special char): ", validate_password)
    age = get_valid_input("Enter your age (10–99): ", validate_age)
    dob = get_valid_input("Enter your Date of Birth (YYYY-MM-DD): ", validate_dob)
    address = get_valid_input("Enter your address (min 10 characters): ", validate_address)

    print("\nAll fields validated successfully.")
    print("Form submitted successfully.")

if __name__ == "__main__":
    main()