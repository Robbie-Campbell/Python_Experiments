from tkinter import *

# Create the frame for the calculator
root = Tk()
root.title("Calculator")
root.configure(background="black")

# Set the frame as not resizable
root.resizable(False, False)

# Define an input  field.
entry = Entry(root, width=40, borderwidth=5)
entry.grid(ipady=5, row=0, column=0, columnspan=3, padx=10, pady=10)


# Inputs the numbers into the input field and appends them onto the end.
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


# Clears all data in the input field.
def button_clear():
    entry.delete(0, END)


# Stores the first number to be added when the equals button is pressed.
def button_plus():
    first_number = entry.get()
    global math
    global f_num
    math = "plus"
    f_num = float(first_number)
    entry.delete(0, END)


# Executes the equals function to return the result of the 2 numbers using the global math variable.
def button_equals():
    number = entry.get()
    entry.delete(0, END)
    if math == "plus":
        entry.insert(0, f_num + float(number))
    elif math == "subtract":
        entry.insert(0, f_num - float(number))
    elif math == "divide":
        entry.insert(0, f_num / float(number))
    else:
        entry.insert(0, f_num * float(number))


# Stores the first number to be divided when the equals button is pressed.
def button_divide():
    first_number = entry.get()
    global math
    global f_num
    math = "divide"
    f_num = float(first_number)
    entry.delete(0, END)


# Stores the first number to be subtracted when the equals button is pressed
def button_subtract():
    first_number = entry.get()
    global math
    global f_num
    math = "subtract"
    f_num = float(first_number)
    entry.delete(0, END)


# Stores the first number to be multiplied when the equals button is pressed
def button_multiply():
    first_number = entry.get()
    global math
    global f_num
    math = "multiply"
    f_num = float(first_number)
    entry.delete(0, END)


# Executes a function which squares the current number in the Entry field
def button_square():
    number = entry.get()
    square = float(number)
    entry.delete(0, END)
    entry.insert(0, float(square * square))


# Define all buttons, set the size an color and what each button does when it is clicked,
# The button click function receives a number when pressed to output onto the input field
button_1 = Button(root, text="1", padx=30, pady=10, command=lambda: button_click(1), bg="White")
button_2 = Button(root, text="2", padx=30, pady=10, command=lambda: button_click(2), bg="White")
button_3 = Button(root, text="3", padx=30, pady=10, command=lambda: button_click(3), bg="White")
button_4 = Button(root, text="4", padx=30, pady=10, command=lambda: button_click(4), bg="White")
button_5 = Button(root, text="5", padx=30, pady=10, command=lambda: button_click(5), bg="White")
button_6 = Button(root, text="6", padx=30, pady=10, command=lambda: button_click(6), bg="White")
button_7 = Button(root, text="7", padx=30, pady=10, command=lambda: button_click(7), bg="White")
button_8 = Button(root, text="8", padx=30, pady=10, command=lambda: button_click(8), bg="White")
button_9 = Button(root, text="9", padx=30, pady=10, command=lambda: button_click(9), bg="White")
button_0 = Button(root, text="0", padx=30, pady=10, command=lambda: button_click(0), bg="White")
button_stop = Button(root, text=".", padx=30, pady=10, command=lambda: button_click("."), bg="White")
button_equals = Button(root, text="=", padx=30, pady=10, command=button_equals, bg="White")
button_plus = Button(root, text="+", padx=30, pady=10, command=button_plus, bg="White")
button_clear = Button(root, text="clear", padx=120, pady=10, command=button_clear, bg="White")
button_divide = Button(root, text="/", padx=30, pady=10, command=button_divide, bg="White")
button_multiply = Button(root, text="*", padx=30, pady=10, command=button_multiply, bg="White")
button_subtract = Button(root, text="-", padx=77, pady=10, command=button_subtract, bg="White")
button_square = Button(root, text="x^2", padx=23, pady=10, command=button_square, bg="White")

# Put the buttons on the screen and lay them out using grid as opposed to the pack method
# This makes sure that the layout is neater.
button_1.grid(row=3, column=0, pady=5)
button_2.grid(row=3, column=1, pady=5)
button_3.grid(row=3, column=2, pady=5)
button_4.grid(row=2, column=0, pady=5)
button_5.grid(row=2, column=1, pady=5)
button_6.grid(row=2, column=2, pady=5)
button_7.grid(row=1, column=0, pady=5)
button_8.grid(row=1, column=1, pady=5)
button_9.grid(row=1, column=2, pady=5)
button_0.grid(row=4, column=1, pady=5)
button_plus.grid(row=6, column=1, pady=5)
button_equals.grid(row=6, column=2, pady=5)
button_clear.grid(row=7, column=0, columnspan=3)
button_divide.grid(row=5, column=0, pady=5)
button_subtract.grid(row=5, column=1, columnspan=2, pady=5)
button_multiply.grid(row=6, column=0, pady=5)
button_stop.grid(row=4, column=2, pady=5)
button_square.grid(row=4, column=0, pady=5)

# Run the program
root.mainloop()
