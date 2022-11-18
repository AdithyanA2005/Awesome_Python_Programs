import csv
from datetime import date
from tabulate import tabulate


# Funtion to add a new row into the csv file
def add_data():
    with open("/home/lucifer/.myapps/pysave/table.csv", "a") as file:
        # CSV Writer Object
        writer = csv.writer(file)

        # Row Details
        amount = input("Enter amount (default: 100): ") or "100"
        reason = input("Enter source (default: Milk): ").title() or "Milk"
        day = input(f"Enter date yyyy-mm-dd (default: {date.today()}): ") or str(date.today())
        print()

        # A Final Conformation
        print("Proceed to add data: ")
        print(tabulate([[amount, reason, day]], tablefmt="heavy_grid"))
        opt = input("Are you sure that you need proceed (y/n): ").lower()
        print()

        # Write to CSV file
        if opt in ["y", "yes"]:
            writer.writerow([amount, reason, day])
            print("NEW DATA ADDED")
        else:
            print("PROCESS CANCELED")


# Function to see the total amount earned
def show_total():
    with open("/home/lucifer/.myapps/pysave/table.csv") as file:
        total = 0
        reader = csv.reader(file)
        for row in reader: total += int(row[0])
        print("THE TOTAL AMOUNT IS:", total)


# Funtion to see the csv as a table
def display_data():
    print("YOUR TABLE IS:")
    with open("/home/lucifer/.myapps/pysave/table.csv") as file:
        rows = csv.reader(file)
        print(tabulate(rows, headers=["AMOUNT", "SOURCE", "DATE"], tablefmt="fancy_grid"))


if __name__ == "__main__":
    print("SAVINGS CSV MANAGER")
    print("-------------------")
    print()

    print("PRESS 1 TO ADD NEW DATA")
    print("PRESS 2 TO SEE THE TABLE")
    print("PRESS 3 TO GET TOTAL AMOUNT")
    print()

    opt = int(input("ENTER YOUR CHOICE: "))
    print()

    if opt == 1: add_data()
    elif opt == 2: display_data()
    elif opt == 3: show_total()
