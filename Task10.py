# Get the student names as input
student_names = input("Enter the student names separated by spaces: ").split()

# Sort the names and create the class roll
class_roll = sorted([name.capitalize() for name in student_names])

# Print the class roll
print("Students:", " ".join(student_names))
print("Class Roll:")
for name in class_roll:
    print(name)
