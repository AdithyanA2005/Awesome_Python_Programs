def character_counter(characters):
    lower_count = upper_count = number_count = special_count = 0
    for i in characters:
        if i.islower():
            lower_count += 1
        elif i.isupper():
            upper_count += 1
        elif i.isdigit():
            number_count += 1
        elif not i.isalnum():
            special_count =+ 1

    return lower_count, upper_count, number_count, special_count


def main():
    query_string = input("Enter your string: ")
    lower_count, upper_count, number_count, special_count = character_counter(query_string)
    print("Number Of Lowercase Characters : ", lower_count)
    print("Number Of Uppercase Characters : ", upper_count)
    print("Number Of Numeric Characters   : ", number_count)
    print("Number Of Special Characters   : ", special_count)


if __name__ == '__main__':
    main()
