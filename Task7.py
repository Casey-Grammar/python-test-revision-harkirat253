# Ask the user for the countdown start number
start = int(input("Time to launch: "))

print("Counting down ...")

# Loop from start down to 1
for i in range(start, 0, -1):
    print(f"{i} ...")

# After countdown finishes
print("Blast Off!")