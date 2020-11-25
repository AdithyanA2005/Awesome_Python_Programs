# This is a sample project to print the list of prime numbers between a given range

# Taking input from the user for first and last limit
start_number = int(input("Enter the 'Starting Limit'"))
stop_number = int(input("Enter the 'Final Limit'"))

# This will print the given numbers
print(f"\nThe prime numbers between {start_number} and {stop_number} are")
for num in range(start_number, stop_number):
    if num >= 2:

        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)

