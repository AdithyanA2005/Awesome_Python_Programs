# The code are in a function 'add_Function' and we will call it from runnable.py
def add_Function():

    # Declarations
    Sum = 0

    # While loop to run this code infinitely many times.
    while True:
        print("Enter the prices and press ENTER 2 times for the total sum")

        # 'UserInput' is the variable used to store the input from user
        UserInput = input()

        # In the If case if we don't press enter button 2 times  it will take input from user
        if UserInput != '' \
                        '':

            # A variable 'Sum is used to produce and store the sum of entered numbers
            Sum = Sum + int(UserInput)

        # In the else case: If the user enter enter button twice the "Sum' will be displayed to the user
        else:
            print(Sum)
            # As we stated a infinity while loop even after showing the sum it will continue to take input from the user
            # So we need to exit from the while loop when the sum is displayed so we use 'break'.
            break
