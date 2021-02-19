# IMPORTING
import time


# Finding the Nth term ny Iteration
def fibIter(n):
    previousNumber = 0
    currentNum = 1
    for i in range(1, n):
        previousPreviousNumber = previousNumber
        previousNumber = currentNum
        currentNum = previousNumber + previousPreviousNumber
    return currentNum


# Finding the Nth term by Recursion
def fibRecur(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fibRecur(n -1) + fibRecur(n - 2)


# MAIN
if __name__ == '__main__':
    # Taking input from user
    num = int(input("Enter a number"))

    # This will be used to calculate the time taken by recursive way
    initRec = time.time()
    print(f"Using recursion value of fib ({num}) is {fibRecur(num)}")
    print(f"It took {time.time() - initRec} seconds")
    # For small values this is faster

    # This will be used to calculate the time taken by iteration way
    initIter = time.time()
    print(f"\nUsing Iteration value of fib ({num}) is {fibIter(num)}")
    print(f"It took {time.time() - initIter} seconds")
    # For big values this is faster
