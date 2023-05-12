# Ezrhael R. Sicat
# BSCpE 1-5
# 05/12/2023
# Simple App Calculator: User will choose one of the four 
# math operations (Addition, Subtraction, Multiplication and Division). 
# User will input 2 numbers and calculate it based on the chosen math operators.

# Import tkinter module to create Graphical User Interface
from tkinter import *

# Create a new window
window = Tk()
window.title("Simple Calculator")
window.geometry("400x200")

# Create a frame to hold the input fields
input_frame = Frame(window)
input_frame.pack()

# Add labels and input fields for the two input values
input1_label = Label(input_frame, text="Input 1:")
input1_label.grid(row=0, column=0)

input1 = Entry(input_frame)
input1.grid(row=0, column=1)

input2_label = Label(input_frame, text="Input 2:")
input2_label.grid(row=1, column=0)

input2 = Entry(input_frame)
input2.grid(row=1, column=1)

# Add a label and drop-down menu for selecting the operator
operator_label = Label(input_frame, text="Select Operator:")
operator_label.grid(row=2, column=0)

operator_var = StringVar(input_frame)
operator_var.set("addition")

operator_options = OptionMenu(input_frame, operator_var, "addition", "subtraction", "multiplication", "division")
operator_options.grid(row=2, column=1)

# Define a function to be called when the button is pressed
def button_press():

    try:
        # Retrieve the values from the input fields and operator selection
        number_one = float(input1.get())
        number_two = float(input2.get())
        operator = operator_var.get()
        
        # Perform the calculation based on the selected operator
        if operator == "addition":
            result = number_one + number_two
        elif operator == "subtraction":
            result = number_one - number_two
        elif operator == "multiplication":
            result = number_one * number_two
        elif operator == "division":
            # Display error when the case is dividing by zero
            if number_two == 0:
                result = "Error: Division by Zero"
            else:
                result = number_one / number_two

        # Update the result label with the calculated value
        result_label.config(text=result)

    # Handle the case of invalid inputs
    except ValueError:
        result_label.config(text="Invalid Input. Try again!")
# Clear the input fields after each calculation
# Add a label and drop-down menu for selecting the operator
# Add a button to trigger the calculation
# Add a label to display the calculated result
result_label = Label(window, text="")
result_label.pack()
# Start the main event loop to keep the window open
window.mainloop()