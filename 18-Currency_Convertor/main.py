# CURRENCY CONVERTER
# -------------------

# First we are opening the file which containing the conversion table
with open('currencyData.txt') as f:
	lines = f.readlines()

# Now we are creating a dictionary to store the table in dictionary format
currencyDict = {}

# Now we are going to take the amount as a input from the user
amount = int(input("Enter the amount: "))
print('\n\n\n')


# Using for loop now we are taking each line from the file
for line in lines:

	# this will split each line
	parsed = line.split("\t")

	# TODO: Write code to select the language using index number

	# We will also print the list of available currency
	print(parsed[0])
	
	# From the divided line we are taking the element assigning the currency to the name
	currencyDict[parsed[0]] = parsed[1]


# Now we are asking the user to enter the currenct name
print("Enter the name of the currency into which you want to convert the amount: ")
currencyChoice = input("Enter the name: ")


# TODO: write some code such that it will be easier for the user to enter the name

#Printing the final converted amount
print(f"{amount} INR is equal to {amount * float(currencyDict[currencyChoice])} {currencyChoice}")
