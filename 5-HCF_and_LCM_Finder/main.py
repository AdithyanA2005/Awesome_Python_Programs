# We are putting the entire code in a function to rerun it
def code():
    # Notice
    print("""Type 'H' to find the HCF or
Type 'L' to find the LCM\n""")
    # Providing the user to choose LCM or HCF and storing it in CAPITAL form
    LcmOrHcf = input("Type Here ")
    LcmOrHcf = LcmOrHcf.capitalize()

    # To store what the user had selected
    varBool = None

    # Declaring what he choice
    if LcmOrHcf == "H":
        print("You choice is to find the HCF\n")
        varBool = True

    elif LcmOrHcf == "L":
        print("You choice is to find the LCM\n")
        varBool = False

    else:
        print("Error while Choosing\n"
              "It is recommended to rerun\n")
        varBool = None

    # Now we are taking the number input from the user
    numberOne = int(input("Enter the first number "))
    numberTwo = int(input("Enter the second number "))
    maxNumber = max(numberOne, numberTwo)

    # This while loop will check different cases
    while True:
        # Using the If case we will find the value The solution of this is given in the file Formula.txt
        if maxNumber % numberTwo == 0 and maxNumber % numberOne == 0:
            # we are creating a variable result to print the result at last
            break

        else:
            # If the above if-case is wrong then we will increase the value of the variable maxNumber by 1
            maxNumber = maxNumber + 1

    # Using the Boolean 'varBool' we created earlier we will print teh final result for the LCM and HCF
    if varBool:
        # In case to find the HCF
        # Step to find the HCF is explained in the file Formula.txt
        result = (numberOne * numberTwo) / maxNumber
        print(f"\nThe HCF of {numberOne} and {numberTwo} is {result}")

    elif varBool is None:
        # If the user selected a Wrong Option
        print("\nYou made a error while selecting for HCF or LCM")

    elif not varBool:
        # In case to find the LCM
        result = maxNumber
        print(f"\nThe LCM of {numberOne} and {numberTwo} is {result}")

    else:
        # In case of not finding the value due to some error
        print("\nThere was some problem with the numbers")


# Welcome
print("""Welcome to the LCM or HCF finder
--------------------------------
\n""")

# This wile true is to repeat the program until the user selects Exit
while True:
    # The user will give input 'CorQ'
    print("""Select: 'C' to Continue or
        'Q' to Exit""")
    CorQ = input("\nSelect Here: ").capitalize()

    # If case will declare whether to continue or exit
    if CorQ == 'C':
        # In case of Continue
        code()
        print("-------------------------------\n\n")

    elif CorQ == 'Q':
        print("Thank you For using our HCF or LCM Finder :)")
        break

    else:
        print("\n\nThat was a Wrong Entry\nEnter once more")
