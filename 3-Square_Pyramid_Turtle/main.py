# IMPORTS
import turtle

# We are creating a variable 'dis' to store the distatnce for the turtle
dis = 0

# we are creating variable 'loop' to store the number of loops
loop = 0

# We will take input from the uesr to stop at which loop
usrinp = int(input("Enter the limit: "))

# We are giving turtle a name
keith = turtle.Turtle()

# To run the code infinitely many times we are using a While loop
while loop != usrinp:
    keith.forward(dis)
    keith.left(90)
    keith.forward(dis)
    keith.left(90)
    dis += 10
    keith.forward(dis)
    keith.left(90)
    keith.forward(dis)
    keith.left(90)
    dis += 10
    keith.forward(dis)
    keith.left(90)
    keith.forward(dis)
    keith.left(90)
    dis += 10
    loop += 1

turtle.done()
