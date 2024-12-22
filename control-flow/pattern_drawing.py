# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks for the current row
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment the row counter
    row += 1
