'''
1 2 3 4 5 6 7 8 9 10
'''
# TODO: MAKE I T A PROJECT
class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")
        print("************")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")
            print("************")

    def cancelTicket(self):
        print(f"Canceling your seat...")
        self.seats = self.seats + 1
        print("Your seat is cancelled")
        print(f"No of seats available is {self.seats}")
        print("************")

intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket()
intercity.getStatus()

