# Now we are creating a function to get
def matrix(m, n):
    matx = []  # This is our main Ouput

    for i in range(m):
        row = []  # This is our row

        for j in range(n):
            # Taking a input
            inp = int(input(f"Enter O[{i}][{j}]"))

            # Appending teh value of inp to the row
            row.append(inp)
        matx.append(row)
    return matx


# Taking the value of m and n as input
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

# Entering the valuie of Matrix A
print("\nEnter Matrix A")
A = matrix(m, n)
print(A)

# Entering the value of matrix B
print("Enter Matrix B")
B = matrix(m, n)

# print
