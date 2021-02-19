from palindrome_finder.main import run

print("WELCOME TO PALINDROME LISTER")
print("\n")

while True:
	print("\n")
	print("Press 'q' to exit Or")
	limit = input("Enter The Limit For The List: ")
	if limit == "q":
		break

	else:
		print("Palindromes: ")
		run(limit)
