def main(arr_1, arr_2):
    print("Array Checker".upper())
    print("_____________")
    print("\n")

    print("Your arrays are: ")
    print(f"    - {arr_1}")
    print(f"    - {arr_2}")

    print("\n")
    flag = sq_ac(arr_1, arr_2)

    if flag:
        print("RESULT: The array values are squares of each other")
    else:
        print("RESULT: The values you have entered is not squares of each other")


def sq_ac(arr_1, arr_2):
    if arr_1 is None or arr_2 is None:
        return False

    if (sorted(arr_1) == sorted([i ** 2 for i in arr_2])) or (sorted(arr_2) == sorted([i ** 2 for i in arr_1])):
        return True

    return False


if __name__ == '__main__':
    array_1 = [1, 2, 3, 4]
    array_2 = [1, 4, 9, 16]
    main(array_1, array_2)
