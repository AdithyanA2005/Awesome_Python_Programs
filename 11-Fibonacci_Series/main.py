import time


def fibRecur(n):
    previousNumber = 0
    currentNum = 1

    for i in range(1, n):
        previousPreviousNumber = previousNumber
        previousNumber = currentNum
        currentNum = previousNumber + previousPreviousNumber

    return currentNum


def main(number):
    initRec = time.time()
    fibRecur(number)
    print(f"Using recursion value of fib ({number}) is {fibRecur(number)}")
    print(f"It took {time.time() - initRec} seconds")


if __name__ == '__main__':
    number = int(input("Enter a number"))
    main(number)
