# Pattern Printer


# Now we are creating two function to create the increase and decrease triangle:-

# For the increasing triangle we are using the function ('increasing')
def increasing(No_Rows):
    # Now we need as much of rows as the users input
    for row in range(0, No_Rows):

        # Now we need as much as columns as the index number of rows; Since we need the Number of column same as index
        # number of rows we need to add it by 1 because the first value is 0 so nothing will be printed there
        for column in range(0, row + 1):
            # Now in place of the column we need to print stars; if we just print the star it will print every star
            # in a new line because end of a printing string is a new-line character, So
            print("*", end=' ')

        # The above will print the stars in a straight line but we need it in a new line, So
        print("")


# Now we are creating the function to print decreasing triangle ('decreasing')
def decreasing(No_Rows):
    # Now we need as much of rows as the users input
    for row in range(0, No_Rows):

        # Now we need as much as columns as in the reverse of index number of rows; Since we need the Number of
        # column in reverse of index number of rows we need to decrease the index number of(row) from the users
        # input(No_Rows) because the first value is 0 so nothing will be printed there
        for column in range(0, No_Rows - row):
            # Now in place of the column we need to print stars; if we just print the star it will print every star
            # in a new line because end of a printing string is a new-line character, So
            print("*", end=' ')

        # The above will print the stars in a straight line but we need it in a new line, So
        print("")


# NOW THE FUNCTION ARE FINISHED

# now first the user should select whether they want to print the stars in increasing or decreasing order using boolean
# we are taking the input in 'int' type as we further want to do calculation's in it
order = int(input("Press '1' to print the triangle in Increasing order\n"
                  "Press '2' to print the triangle in Decreasing order\n"
                  "ENTER THE NUMBER:\n"))

# After this we should take the input of number of rows from the user('No_Rows') which will be printed we will
# take input in 'int' type as we further want to do more calculations in it
No_Rows = int(input("Enter the number of rows:\n"))

# We are creating a boolean, If it is true then we will print the triangle in Increasing order else in decreasing
orderType = bool(order == 1)

if orderType == 1:
    increasing(No_Rows)
elif orderType == 0:
    decreasing(No_Rows)
else:
    print("Unknown error")
