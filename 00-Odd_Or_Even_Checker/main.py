def main():
    print("\n")
    print("ODD OR EVEN CHECKER")
    print("-------------------")
    print("\n")
    print("Press 'Q' to exit or")
    print("Enter a number to get started")

    while True:
        print("\n")
        number = input("Enter Number => ")

        if number == "q":
            print("\n")
            print("closing".upper())
            break

        elif number == "Q":
            print("\n")
            print("closing".upper())
            break

        else:
            number = int(number)
            odd_or_even = is_odd(number)

            if odd_or_even:
                print(f"The Number {number} is a Odd Number")

            else:
                print(f"The Number {number} is a Even Number")


def is_odd(number):
    floor_number = number % 2

    if floor_number == 1:
        return True

    elif floor_number == 0:
        return False


if __name__ == "__main__":
    main()
