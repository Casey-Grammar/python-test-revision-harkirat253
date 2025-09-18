# Ask user for first and last name
full_name = input("First and Last Name? ")

# Split input into first name and last name
first, last = full_name.split()

# Take first 2 letters of first name
part1 = first[:2]

# Take last 4 letters of last name
part2 = last[-4:]

# Combine them
call_sign = part1 + part2

# Output the result
print("The new call sign is:", call_sign)
