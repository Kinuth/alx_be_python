size_of_pattern = int(input("Enter the size of the pattern: "))
row = 1
while row <= size_of_pattern:
    for _ in range(size_of_pattern):
        print("*", end="")
    print()  # Move to the next line after printing each row
    row += 1
# This program draws a square pattern of asterisks based on user input.