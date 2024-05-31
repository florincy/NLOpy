import tkinter as tk
from PIL import Image, ImageTk
from Frontend.DataAnalysis import DataAnalysis
from Frontend.Home import Home
from Frontend.InputBuilder import InputBuilder
import os

#Creating GUI window
root = tk.Tk()
root.geometry('750x750')
home_window = Home(root)
min_w = 45  # Minimum width of the frame
max_w = 150  # Maximum width of the frame
cur_width = min_w  # Current width of the frame
expanded = False  # Check if it is completely expanded

#Paths to icon images
current_dir = os.path.dirname(__file__)
home_path = os.path.join(current_dir, 'home.png')
data_path = os.path.join(current_dir, 'keys.png')
input_path = os.path.join(current_dir, 'input.png')
exit_path = os.path.join(current_dir,'close.png')

#Expand the GUI window 
def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = root.after(5, expand)  # Repeat this function every 5 ms
    frame.config(width=cur_width)  # Change the width to the new increased width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expanded
        root.after_cancel(rep)  # Stop repeating the function
        fill()
        
#Contract the GUI window 
def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = root.after(5, contract)  # Call this function every 5 ms
    frame.config(width=cur_width)  # Change the width to the new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        root.after_cancel(rep)  # Stop repeating the function
        fill()
        
#Filling side menu with icons and buttons
def fill():
    if expanded:  # If the frame is expanded
        # Show text on buttons, and remove the images
        home_b.config(text='Home', image='', font=("Calibri", 16, "italic", "bold"))
        data_analysis_b.config(text='Data Analysis', image='', font=("Calibri", 16, "italic", "bold"))
        input_builder_b.config(text='Input Builder', image='', font=("Calibri", 16, "italic", "bold"))
        exit_b.config(text='Exit', image='', font=("Calibri", 16, "italic", "bold"))
    else:
        # Show images on buttons
        home_b.config(image=home, font=("Calibri", 16, "italic", "bold"))
        data_analysis_b.config(image=data_analysis, font=("Calibri", 16, "italic", "bold"))
        input_builder_b.config(image=input_builder, font=("Calibri", 16, "italic", "bold"))
        exit_b.config(image=exit, font=("Calibri", 16, "italic", "bold"))

#Quit the GUI application
def quit_app():
    root.destroy()
    
#NLO data analysis redirectioning function, instatiate object from class 
def data_analysis_application(): 
    data_analysis_app = DataAnalysis(root)
    
#Home redirectioning function
def home_function():
    home_window = Home(root)  

#Input bulding redirectioning function
def input_builder_function():
    input_builder_app=InputBuilder(root)
    
# Define the icons to be shown and resize them
home = ImageTk.PhotoImage(Image.open(home_path).resize((40, 40), Image.ANTIALIAS))
data_analysis = ImageTk.PhotoImage(Image.open(data_path).resize((40, 40), Image.ANTIALIAS))
input_builder = ImageTk.PhotoImage(Image.open(input_path).resize((40, 40), Image.ANTIALIAS))
exit = ImageTk.PhotoImage(Image.open(exit_path).resize((40, 40), Image.ANTIALIAS))

root.update()  # Update the root window for the width to get updated
frame = tk.Frame(root, bg='#7C98B3', width=50, height=root.winfo_height())
frame.grid(row=0, column=0)

# Make the buttons with the icons to be shown
home_b = tk.Button(frame, image=home, bg='#7C98B3', relief='flat', command=home_function, borderwidth=0, highlightthickness=0)
data_analysis_b = tk.Button(frame, image=data_analysis, bg='#7C98B3', relief='flat', command=data_analysis_application, borderwidth=0, highlightthickness=0)
input_builder_b = tk.Button(frame, image=input_builder, bg='#7C98B3', relief='flat', command=input_builder_function,borderwidth=0, highlightthickness=0)
exit_b = tk.Button(frame, image=exit, bg='#7C98B3', relief='flat', command=quit_app, borderwidth=0, highlightthickness=0)

# Put them on the frame
home_b.grid(row=0, column=0, pady=10)
data_analysis_b.grid(row=1, column=0, pady=50)
input_builder_b.grid(row=2, column=0)
exit_b.grid(row=5, column=0, pady=50)

# Bind to the frame, if entered or left
frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

root.mainloop()
