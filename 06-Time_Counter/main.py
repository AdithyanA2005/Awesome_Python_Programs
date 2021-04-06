import time


def counter(count):
    limit = count

    while count:
        minute, second = divmod(count, 60)

        timer = "{:02d}:{:02d}".format(minute, second)
        print(f"TIME: {timer}", end="\r")

        time.sleep(1)
        count = count - 1

    print(f"Your timer for {limit} second is over")
    print("Program Finished")


def main():
    print("WELCOME TO ADI'S COUNTER")
    print("------------------------")
    print("\n")

    print("To Start Enter The Time In Seconds")
    limit = input("Seconds: ")
    print("\n")

    print("Timer Started")
    print("Press 'Ctrl' + 'C' To stop at anytime")
    print("\n")

    limit = int(limit)
    counter(limit)


if __name__ == '__main__':
    main()
