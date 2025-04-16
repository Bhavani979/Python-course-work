''' Employee Information to Collected:
Employee ID (int)

Employee Name (str)

Salary (float)

Departments (list) – Comma-separated

Attendance Details (tuple) – Days present and absent

Bonus Percentage (float)

Skills (set) – Unique skills
Contact Info (dict) – Email, Phone, and City

'''

employee_id = int(input("Enter Employee ID: "))
employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

departments_input = input("Enter exactly 3 Departments (comma-separated): ")
departments = departments_input.split(',')

days_present = int(input("Enter Days Present: "))
days_absent = int(input("Enter Days Absent: "))
attendance_details = (days_present, days_absent)

bonus = float(input("Enter Bonus Percentage: "))

skills_input = input("Enter exactly 3 Skills (comma-separated): ")
skills = set(skills_input.split(','))

email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
city = input("Enter City: ")

contact_info = {
    "Email": email,
    "Phone": phone,
    "City": city
}

# Task 2: Displaying Using Different Formatting Methods

print("\n--- Employee Information ---\n")

# 1. Comma Separation
print("Employee ID, Name, Salary:", employee_id, employee_name, salary, sep=',')

# 2. Percentage Formatting
print("Bonus Percentage: %.2f%%" % bonus)

# 3. f-strings
print(f"\nEmployee Name: {employee_name}")
print(f"Salary: ₹{salary:.2f}")
print(f"Bonus: {bonus}%")
print(f"Days Present: {attendance_details[0]} days")
print(f"Days Absent: {attendance_details[1]} days")

# 4. .format() method
print("\nContact Info: Email - {0}, Phone - {1}, City - {2}".format(
    contact_info["Email"], contact_info["Phone"], contact_info["City"]
))

