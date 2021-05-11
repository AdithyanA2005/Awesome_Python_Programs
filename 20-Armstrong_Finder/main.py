from tkinter import *
from finder import main_func


def verify():
    # This will print result in terminal
    print(f'\nValue entered is {InpNumber.get()}')

    # we are storing it in a variable
    result = main_func(InpNumber.get())

    # Printing result in terminal
    print(result)     

    # Clearing the existing text in the Entry box in the GUI
    InpNumber.set("")

    # This will print the result in the output section of GUI
    Result.set(Result.get() + result + "\n")

    # This function will return the value as result
    return result



# This is the starting
root = Tk()

# This is the window size
root.geometry("400x650")

# This is the window 
root.title("Armstrong Checker")

# This is the configurations
root.configure(bg='#856ff8')

# This is the variable to store input value
InpNumber = StringVar()

# This is the variable to store result
Result = StringVar()

# This is the Title of the page
f0 = Frame(root, width=400, height=70)

# This is the heading
Label(f0, text="Armstrong Checker", bg="purple", padx=50, fg="white", font="lucida 30 bold").pack()

#This will pack f0
f0.pack()

# This is a indication label
Label(text="Enter the number below", pady=25, fg="white", bg="#856ff8", font="lucida 20").pack()

# This is the Entry field
entry = Entry(root, width=20, textvariable=InpNumber, fg="#856ff8", bg="white", font="lucida 20").pack()

# This is a dummy label used to get some space between input and submit button
Label(bg="#856ff8").pack()

# This is the push button
Button(root, text="Verify", command=verify, activeforeground="purple", activebackground="white", bg="purple", fg="white", width=20, height=1, font=20).pack()

# This is a dummy label used to get some space between input and submit button
Label(bg="#856ff8", height=3).pack()

# This is the output Title
Label(text="Output", width=30, bg="green", fg="white", font="lucida 14").pack()

# This is the output field
output = Label(textvariable=Result, bg="#569c77", fg="purple", width=30, height=14, font="lucida 14").pack()

# This will show the codes 
root.mainloop()

