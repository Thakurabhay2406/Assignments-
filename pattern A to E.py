n = 5  # Number of letters from A to E

for i in range(n):
    # Left side letters
    for j in range(n - i):
        print(chr(65 + j), end=" ")
    
    # Spaces in the middle
    print("  " * (2 * i - 1), end="")
    
    # Right side letters (skip middle letter if i > 0)
    if i != 0:
        for j in range(n - i - 1, -1, -1):
            print(chr(65 + j), end=" ")
    else:
        for j in range(n - i - 2, -1, -1):
            print(chr(65 + j), end=" ")
    
    print()
