import tkinter as tk

class InitialLayout:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLOpy")
        
        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(master)
        self.widget_frame.pack()  # Expand to fill the available space
        
        # Centering the frame on the window
        self.widget_frame.grid_rowconfigure(0, weight=1)
        self.widget_frame.grid_columnconfigure(0, weight=1)
        
        # NLO data app label
        self.msg = tk.Label(self.widget_frame, text="NLOpy", font=("Calibri", 16, "italic", "bold"))
        self.msg.grid(row=0, columnspan=3)
        
        # Button to switch to the input builder layout
        self.switch_to_input_builder = tk.Button(self.widget_frame, text="Input Builder", command=self.switch_to_input_builder,font=("Calibri", 12), fg="white", bg='#011627')
        self.switch_to_input_builder.grid(row=1, column=0, padx=5)

        # Button to switch to the third layout
        self.switch_to_NLO_data = tk.Button(self.widget_frame, text="Data analysis", command=self.switch_to_NLO_data,font=("Calibri", 12), fg="white", bg='#011627')
        self.switch_to_NLO_data.grid(row=1, column=1, padx=5)

        # Exit button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy,font=("Calibri", 10), fg='#011627', width=5, highlightcolor="#011627", highlightthickness=2, highlightbackground='#011627')
        self.exit_button.pack()

    def switch_to_input_builder(self):
        self.master.destroy()  # Destroy the current window
        new_root = tk.Tk()  # Create a new window
        InputBuilder(new_root)  # Switch to the input builder layout

    def switch_to_NLO_data(self):
        self.master.destroy()  # Destroy the current window
        third_root = tk.Tk()  # Create a new window
        ThirdLayout(third_root)  # Switch to the third layout

    def switch_to_initial_layout(self):
        pass

class InputBuilder:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO Input Builder")
        
        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(master)
        self.widget_frame.pack()  # Expand to fill the available space
        
        # Centering the frame on the window
        self.widget_frame.grid_rowconfigure(1, weight=1)
        self.widget_frame.grid_columnconfigure(1, weight=1)
        
        # NLO input builder label
        self.msg = tk.Label(self.widget_frame, text="NLO Input Builder", font=("Calibri", 16, "italic", "bold"))
        self.msg.grid(row=0, columnspan=3)
        
        # Create a frame to contain the buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        # Centralize the buttons horizontally
        self.button_frame.grid_rowconfigure(5, weight=1)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Back to initial layout button
        self.back_to_initial_button = tk.Button(self.button_frame, text="Back to Initial Layout", command=self.switch_to_initial_layout)
        self.back_to_initial_button.grid(row=5, column=0, padx=5)

        # Exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=5, column=1, padx=5)

    def switch_to_initial_layout(self):
        self.master.destroy()  # Destroy the current window
        initial_root = tk.Tk()  # Create a new window
        InitialLayout(initial_root)  # Switch to the initial layout

class ThirdLayout:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO Data")
        
        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(master)
        self.widget_frame.pack()  # Expand to fill the available space
        
        # Centering the frame on the window
        self.widget_frame.grid_rowconfigure(0, weight=1)
        self.widget_frame.grid_columnconfigure(0, weight=1)
        
        # NLO data label
        self.msg = tk.Label(self.widget_frame, text="NLO Data", font=("Calibri", 16, "italic", "bold"))
        self.msg.grid(row=0, columnspan=3)
        
        # Button to switch back to the initial layout
        self.switch_to_initial_layout = tk.Button(self.widget_frame, text="Switch to Initial Layout", command=self.switch_to_initial_layout)
        self.switch_to_initial_layout.grid(row=1, column=0, columnspan=3, pady=10)

    def switch_to_initial_layout(self):
        self.master.destroy()  # Destroy the current window
        initial_root = tk.Tk()  # Create a new window
        InitialLayout(initial_root)  # Switch to the initial layout

# Create the initial layout
root = tk.Tk()
app = InitialLayout(master=root)
root.mainloop()
