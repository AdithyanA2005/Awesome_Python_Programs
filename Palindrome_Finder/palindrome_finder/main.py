
def run(limit):
    limit = int(limit)
    no_of_palindrome = 0

    for num in range(10, limit + 1):
        temp = num
        reverse = 0

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10

            if num == reverse:
                no_of_palindrome = no_of_palindrome + 1
                print(f"          - {reverse}")

    print(f"    There are total {no_of_palindrome} number of palindromes between 10 and {limit} ")