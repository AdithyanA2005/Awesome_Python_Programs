
def main_func(n):
    """    
    This file contain the main function that is brain of the function
    """

    # This is to convert the string variable to a integer
    n = int(n)
    
    # Adding a variable with value 0 to store the calculation
    Sum = 0

    # To find the power by which the digits should be raised to
    order = len(str(n))

    # While getting the fina result we need to check whether the value is equal to  Sum so we are creating  a copy of n
    copyOfN = n

    # Creating  awhile loop to run teh calculation repeatedly
    while n > 0:

        # Taking each digit from the number to raise it to the value 'order'
        digit = n % 10
	
        # Increasing te value of the sum by adding it with the value of digit raise to the power 'order'
        Sum += digit ** order

	# Cutting out each digit from the number after the operations
        n = n // 10

        # Storing result in a variable whether the number is equal to the sum or Is the number a Armstrong number
        if Sum == copyOfN :  # This is for Armstrong number
            result = (f"{copyOfN} is a Armstrong number")
        
        else:  # This is not for Armstrong number
            result = (f"{copyOfN} is not a Armstrong number") 

        # This will return the result
        return result

