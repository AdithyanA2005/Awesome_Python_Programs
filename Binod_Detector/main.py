# IMPORTS
import os


# This function will check whether the binod is present
def isBinod(filename):

	# First we will opent the file in read mode
	with open(filename, "r") as f:

		# Then we will read the contents
		fileContent = f.read()

	# Now we will look in the txt file for the word binod in any structure so we are using lowercase to convert the txt into lower case
	if "binod" in fileContent.lower():
		return True
	
	else:
		return False



# START
if __name__ == "__main__":

	# This will list the comtents in the directory
	dir_contents = os.listdir()

	# This will represent the number of Binods
	nBinod = 0

	# This is the condition for each elemenet in the directory
	for item in dir_contents:

		# This will check whether the file end with '.txt' extention or is it a text file, only the text file we wiill detect binod
		if item.endswith('txt'):

			# This will print a status to the user
			print(f"\nDetecting Binod in {item}")

			# In a variable flag now we will get the status of the binod detection
			flag = isBinod(item)
			
			if flag:
				print(f"Binod found in {item}")
				#If the binod is found then the number of binod is increased by 1
				nBinod += 1

			else:
				print(f"Binod not found in {item}")

	# Printing the final summary and result
	print("\n\n****BINOD DETECTOR SUMMARY*****\n")
	print(f"{nBinod} files found with Binod hidden into them")
