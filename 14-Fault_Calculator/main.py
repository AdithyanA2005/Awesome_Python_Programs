# FAULTY CALCULATOR IS A CALCULATOR WHICH WILL GIVE CORRECT ANSWER EXCEPT SOME SELECTED ONE
# This is a calculator shows the wrong answer for :
# 56 + 6 = 4
# 43 - 3 = 30
# 55 * 2 = 100
# 40 / 2 = 40


# The function 'addition' is used to add the two inputs
def addition(add1, add2):
    add1 = int(add1)
    add2 = int(add2)
    if add1 != 56 or add2 != 6:
        Sum = add1 + add2
        print(f"{add1} + {add2} = {Sum}\n\n")
    else:
        print(f"{add1} + {add2} = 4\n\n")


# The function 'subtraction' is used to add the two input
def subtraction(sub1, sub2):
    sub1 = int(sub1)
    sub2 = int(sub2)
    if sub1 != 43 and sub2 != 3:
        Diff = sub1 - sub2
        print(f"{sub1} - {sub2} = {Diff}\n\n")
    else:
        print(f"{sub1} - {sub2} = 30\n\n")


# The function 'multiplication' is used to add the two input
def multiplication(mul1, mul2):
    mul1 = int(mul1)
    mul2 = int(mul2)
    if mul1 != 55 and mul2 != 2:
        multi = mul1 * mul2
        print(f"{mul1} x {mul2} = {multi}\n\n")
    else:
        print(f"{mul1} x {mul2} = 100\n\n")


# The function 'division' is used to add the two input
def division(div1, div2):
    div1 = int(div1)
    div2 = int(div2)
    if div1 != 43 and div2 != 3:
        Divi = div1 / div2
        print(f"{div1} / {div2} = {Divi}\n\n")
    else:
        print(f"{div1} / {div2} = 40\n\n")


# We are using the 'WHILE' loop to run the code infinitely many times such that the user doesn't
# want to rerun the program for more input
while True:

    # We are creating a variable 'arithmeticOperation' to choose which operation to perform
    arithmeticOperation = input("CHOOSE YOUR CHOICE:- \n"
                                "Press 'A' for Addition\n"
                                "Press 'S' for Subtraction\n"
                                "Press 'M' for Multiplication\n"
                                "Press 'D' for Division\n"
                                "Press 'E' to Cancel Operation\n"
                                "Press 'Q' to Exit\n\n"
                                "Enter the operation:-"
                                ).capitalize()

    # NOTE:
    # Using if case we are checking whether the user have chosen a
    # operation or chose to quit or entered something wrong
    # and we also need to get the input for numbers

    # ADDITION
    if arithmeticOperation == "A":
        print("You have selected Addition")

        # We are creating a input for the first number
        num1 = input("Enter first numbers").capitalize()

        # Now we also want to give user a choice to cancel operation
        if num1 == "E":
            continue
        else:
            print(f"First number is {num1} \n")

        # We are creating a input for the Second number
        num2 = input("Enter second number").capitalize()

        # Now we also want to give user a choice to cancel operation
        if num2 == "E":
            continue
        else:
            print(f"Second number is {num2} \n")

        # If user doest cancel while entering the number we should show the result
        # Using the 'addition' function
        addition(num1, num2)

    # SUBTRACTION
    elif arithmeticOperation == "S":
        print("You have selected Subtraction")

        # We are creating a input for the first number
        num1 = input("Enter first numbers").capitalize()

        # Now we also want to give user a choice to cancel
        if num1 == "E":
            continue
        else:
            print(f"First number is {num1} \n")

        # We are creating a input for the Second number
        num2 = input("Enter second number").capitalize()

        # Now we also want to give user a choice to cancel
        if num2 == "E":
            continue
        else:
            print(f"Second number is {num2} \n")

        # If user doest cancel while entering the number we should show the result
        # Using the 'subtraction' function
        subtraction(num1, num2)

    # MULTIPLICATION
    elif arithmeticOperation == "M":
        print("You have selected Multiplication")

        # We are creating a input for the first number
        num1 = input("Enter first numbers").capitalize()

        # Now we also want to give user a choice to cancel
        if num1 == "E":
            continue
        else:
            print(f"First number is {num1} \n")

        # We are creating a input for the Second number
        num2 = input("Enter second number").capitalize()

        # Now we also want to give user a choice to cancel
        if num2 == "E":
            continue
        else:
            print(f"Second number is {num2} \n")

        # If user doest cancel while entering the number we should show the result
        # Using the 'multiplication' function
        multiplication(num1, num2)

    # DIVISION
    elif arithmeticOperation == "D":
        print("You have selected Division")

        # We are creating a input for the first number
        num1 = input("Enter first numbers").capitalize()

        # Now we also want to give user a choice to cancel
        if num1 == "E":
            continue
        else:
            print(f"First number is {num1} \n")

        # We are creating a input for the Second number
        num2 = input("Enter second number").capitalize()

        # Now we also want to give user a choice to cancel
        if num2 == "E":
            continue
        else:
            print(f"Second number is {num2} \n")

        # If user doest cancel while entering the number we should show the result
        # Using the 'division' function
        division(num1, num2)

    # EXIT
    elif arithmeticOperation == "Q":
        print("Thank you for using the fault calculator")
        break

    else:
        print('error')
        continue
