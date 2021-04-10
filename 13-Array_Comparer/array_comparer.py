def main():
    print("array checker".upper())
    print("_____________")
    print("\n")

    print("Enter array as ',' separated values")
    print("\n")

    arr_inp_one = input("Enter 1'st Array: ")
    arr_inp_two = input("Enter 2'nd Array: ")

    arr_one = arr_inp_one.split(',')
    arr_two = arr_inp_two.split(',')

    print("Your arrays are: ")
    print(f"    - {arr_one}")
    print(f"    - {arr_two}")

    print("\n")
    flag = check(arr_one, arr_two)

    if flag:
        print("RESULT: Yes, The Arrays Match Each Other")
    else:
        print("RESULT: No, The Arrays Doesn't Match Each Other")

    print("___________________________________________")
    print("___________________________________________")


def check(arr1, arr2):
    if len(arr1) != len(arr2):
        print("failed!!".upper())
        print("Number of values were different for arrays")

    else:
        length = len(arr1)
        for i in range(0, length):
            if str(arr1[i]) != str(arr2[i]):
                flag = False
                break
            else:
                flag = True
        return flag


if __name__ == '__main__':
    main()
