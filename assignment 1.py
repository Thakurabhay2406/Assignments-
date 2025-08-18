rows = 4  # number of rows

for i in range(1, rows + 1):       # Outer loop for rows
    for j in range(1, i + 1):      # Inner loop for numbers
        print(j, end="")           # Print numbers in the same line
    print()                        # Move to the next line
