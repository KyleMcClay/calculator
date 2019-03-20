"""
11/18/2018
Graphic Calculator - using tkinter
sample code by Geeksforgeeks.com
https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
#C:\Users\ksmcc\PycharmProjects\Calculator\Main.py
"""

from tkinter import *

# Python program to  create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

#constants
button_color = "black"
button_background_color = "light gray"
button_height = 1
button_width = 8

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""

        # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""

    # Function to clear the contents


# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light gray")

    # set the title of GUI window
    gui.title("Calculator")

    # set the configuration of GUI window
    gui.geometry("265x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    equation.set('enter your expression')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg= button_color, bg=button_background_color,
                     command=lambda: press(1), height=button_height, width=button_width)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(2), height=button_height, width=button_width)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(3), height=button_height, width=button_width)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(4), height=button_height, width=button_width)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(5), height=button_height, width=button_width)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(6), height=button_height, width=button_width)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(7), height=button_height, width=button_width)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(8), height=button_height, width=button_width)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(9), height=button_height, width=button_width)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg=button_color, bg=button_background_color,
                     command=lambda: press(0), height=button_height, width=button_width)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg=button_color, bg=button_background_color,
                  command=lambda: press("+"), height=button_height, width=button_width)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg=button_color, bg=button_background_color,
                   command=lambda: press("-"), height=button_height, width=button_width)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg=button_color, bg=button_background_color,
                      command=lambda: press("*"), height=button_height, width=button_width)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg=button_color, bg=button_background_color,
                    command=lambda: press("/"), height=button_height, width=button_width)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg=button_color, bg=button_background_color,
                   command=equalpress, height=button_height, width=button_width)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg=button_color, bg=button_background_color,
                   command=clear, height=button_height, width=button_width)
    clear.grid(row=5, column='1')

    carrot = Button(gui, text=' ^ ', fg=button_color, bg=button_background_color,
                    command=lambda: press("*"*2), height=button_height, width=button_width)
    carrot.grid(row=6, column=0)

    left_parentheses = Button(gui, text=' ( ', fg=button_color, bg=button_background_color,
                    command=lambda: press("("), height=button_height, width=button_width)
    left_parentheses.grid(row=6, column=1)

    right_parentheses = Button(gui, text=' ) ', fg=button_color, bg=button_background_color,
                    command=lambda: press(")"), height=button_height, width=button_width)
    right_parentheses.grid(row=6, column=2)

    backspace = Button(gui, text=' <-- ', fg=button_color, bg=button_background_color,
                    command=backspace, height=button_height, width=button_width)
    backspace.grid(row=6, column=3)

    # start the GUI
    gui.mainloop()
