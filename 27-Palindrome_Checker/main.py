def checker(value):
    mid_of_value = int(len(value)/2)    
    back_value = 0
    for i in range(mid_of_value):
        if value[i] == value[back_value]:
            back_value -= 1
        else:
            print(f"'{value}' is not a palindrome number")
            break
    else:
        print(f"'{value}' is a palindrome number")


def main():
    query_number = input("Enter Number")
    if query_number.isdigit():
        checker(query_number)
    else:
        print("The input that was given is not a numeric value")
        print("Exiting...")


if __name__ == '__main__':
    main()
