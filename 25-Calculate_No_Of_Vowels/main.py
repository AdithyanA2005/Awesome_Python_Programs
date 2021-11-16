def main(query):
    vowel_count = 0

    for i in query:
        if i.upper() in "AEIOU":
            vowel_count += 1

    print("\n")
    print(f"There are {vowel_count} vowels in the string you entered")


if __name__ == '__main__':
    main(input("Enter String: "))
