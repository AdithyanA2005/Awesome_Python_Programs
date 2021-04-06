def palindrome(limit):
    limit = int(limit)
    no_of_palindrome = 0

    for num in range(0, limit + 1):
        temp = num
        reverse = 0

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10

            if num == reverse:
                no_of_palindrome = no_of_palindrome + 1
                print(f"          - {reverse}")

    print(f"    => From the number 0 - {limit}")
    print(f"    => There are {no_of_palindrome} Palindromes")


def main():
    print("WELCOME TO PALINDROME LISTER")
    print("----------------------------")

    while True:
        print("\n")
        print("Press 'q' to exit Or")
        limit = input("Enter The Limit For The List: ")
        if limit == "q":
            break

        else:
            print("Palindromes: ")
            palindrome(limit)


if __name__ == "__main__":
    main()
