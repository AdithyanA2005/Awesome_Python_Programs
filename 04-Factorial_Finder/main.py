# PROGRAM TO FIND THE FACTORIAL OF THE ENTERED NUMBER


# We are creating a function to print the factorial of a number
def factorial(Number):
    # Let us assign the default value of factorial as '1'
    Factorial = 1

    # We should increase the value by one
    Number = Number + 1

    # This is the if case for negative digits
    if Number < 0:
        return "Factorial of a number can't be a negative digit"

    # This is the if else case if the number is '0'
    elif Number == 0:
        return 1

    # This is the main program to find the factorial
    else:
        for i in range(1, Number):
            Factorial = Factorial * i

        # Now we should print the factorial of the number
        return Factorial


if __name__ == '__main__':
    while True:
        # We are taking the number as input from the user
        number = int(input("Enter the number"))

        # We are storing the value of factorial in the variable 'result'
        result = factorial(number)

        # Now we are printing the final result
        print(f"The factorial of the number {number} is {result}")
