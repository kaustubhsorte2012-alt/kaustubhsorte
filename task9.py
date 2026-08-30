# Create a dictionary of student marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88,
    "Rohan": 75
}

# Ask the user to enter a student's name
name = input("Enter student's name: ")

# Retrieve and display the marks
if name in students:
    print("Marks of", name, ":", students[name])
else:
    print("Student not found.")