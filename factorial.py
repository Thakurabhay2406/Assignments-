def factorial(number):

    if number == 0 or number == 1:

        return 1

    else:

        result = 1

        for I in range(2, number + 1):

            result *= I

        return result

number = int(input("Enter a number to calculate its factorial: "))

print(factorial(number))
