# HEALTH MANAGEMENT SYSTEM


# => Importing Modules that are used
import datetime


# => We are creating a function 'OpenWriteClose' to open or create a file, store the input and close the file
def OpenWriteClose(f):

    f.write(input(getDate()) + "\n")
    print("Saved Successfully")
    f.close()


# => We want to create a function to print the date 'getDate'
def getDate():
    # We are using the datetime module to print the time
    Date = datetime.datetime.now()

    # we just want the Date(year, month, date) and Time(hour, minutes); so we are changing the date into string type
    # to use array in it
    Date = str(Date)
    print("DATE:", Date[0:11])
    print("TIME:", Date[11:16])
    return "Schedule: "


# => WELCOME
# This is a welcome statement for the user
print("Welcome to Health Management system")

# We are asking the user whether he want to new or retrieve using the int variable 'WriteOrRetrieve'
print("Do you want to write or retrieve the type\n "
      "50 to add New, 60 to see Saved:\n")
WriteOrRetrieve = int(input("Enter your choice: "))


# => IF-CASE
# We are creating a if case to check whether the user had chosed to add or retrieve

# If the user choose to add new
if WriteOrRetrieve == 50:
    # Now user need to choose the client name subclass
    Client = int(input("\nWhose plan do you want press\n "
                       "1 for Adithyan, 2 for Deepa, 3 for Anilkumar:"))
    Options = int(input("\nWhat do you want press\n "
                        "1 for Diet, 2 for Exercise:"))

    # Now we are creating specific cases for the clients and subclass
    if Client == 1 and Options == 1:  # Adithyan's diet
        OpenWriteClose(open("Adithyan_Diet.txt", "a"))


    elif Client == 1 and Options == 2:  # Adithyan's exercise
        OpenWriteClose(open("Adithyan_Exercise.txt", "a"))

    elif Client == 2 and Options == 1:  # Deepa's diet
        OpenWriteClose(open("Deepa_Diet.txt", "a"))

    elif Client == 2 and Options == 2:  # Deepa's exercise
        OpenWriteClose(open("Deepa_Exercise.txt", "a"))

    elif Client == 3 and Options == 1:  # Anilkumar's diet
        OpenWriteClose(open("Anilkumar_Diet.txt", "a"))

    elif Client == 3 and Options == 2:  # Anilkumar's exercise
        OpenWriteClose(open("Anilkumar_Exercise.txt", "a"))

elif WriteOrRetrieve == 60:
    # As earlier, Now user need to choose the client name subclass
    Client = int(input("\nWhose Plan do you want to retrive\n "
                       "1 for Harry, 2 for Rohan, 3 for Hammad:"))

    Options = int(input("\nWhat do you want press\n "
                        "1 for Diet, 2 for Exercise:"))

    if Client == 1 and Options == 1:





        f = open("Adithyan_Diet.txt")

        content = f.read()

        print("\nThe Diet suggested is")

        print(getDate(), "\n", content, )

        f.close()

#
#     def fun():
#
#         a = int(input("1 for Harry, 2 for Rohan, 3 for Hammad:"))
#
#         b = int(input("1 for Diet, 2 for Exercise:"))
#
#
#
# fun()
