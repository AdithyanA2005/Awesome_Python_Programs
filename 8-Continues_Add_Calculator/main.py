def main():
    total_sum = 0

    print("WELCOME BACK")
    print("------------")
    print("\n")

    print("usage:".upper())
    print("     - Press 'ENTER' To Add Value")
    print("     - Press 'S' To Show Total")
    print("     - Press 'Q' To Cancel Process")
    print("\n")

    print("start enterign".upper())
    while True:

        try:
            user_input = input("    -> ")

            # If User Input is 'S'
            if user_input.upper() == 'S':
                print("\n")
                print(f"    TOTAL SUM: {total_sum}")
                break

            # If User Input is 'Q'
            elif user_input == 'Q':
                print("\n")
                print("     Operation Cancelled")
                break

            # If user input is anything else probably a integer
            else:
                total_sum = total_sum + int(user_input)

        except Exception as e:
            print("\n")
            print("     Error Occured")
            print("     This value will be ignored")
            print("\n")


if __name__ == "__main__":
    main()
