def dog_to_human_age(dog_years):
    human_age = dog_years * 7
    return human_age

# Get user input for dog's age
dog_years = int(input("Dog years: "))

# Convert dog years to human years
human_age = dog_to_human_age(dog_years)

# Print the result
print(f"Human age = {human_age}")
