# Read in the cat names
cat_names = input("Enter the cat names separated by spaces: ").split()

# Count the number of cats
num_cats = len(cat_names)

# Print the result
print(f"Cats: {' '.join(cat_names)}")
print(f"You have {num_cats} cats.")
