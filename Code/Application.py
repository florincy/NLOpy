class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO data app")
        
        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(master)
        self.widget_frame.pack()# Expand to fill the available space
        
        # Centering the frame on the window
        self.widget_frame.grid_rowconfigure(0, weight=1)
        self.widget_frame.grid_columnconfigure(0, weight=1)
        

        # NLO data app label
        self.msg = tk.Label(self.widget_frame, text="NLO data app", font=("Calibri", 16, "italic", "bold"))
        self.msg.grid(row=0, columnspan=3)

        # Select Input Directory label and button
        self.select_input_label = tk.Label(self.widget_frame, text="Choose .log files directory:", font=("Calibri", 10, "bold"))
        self.select_input_label.grid(row=1, column=0, sticky=tk.W)
        self.select_dir_button_input = tk.Button(self.widget_frame, text="Choose directory", command=self.select_directory_input, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_input.grid(row=1, column=1, sticky=tk.W)
        self.selected_directory_label_input = tk.Label(self.widget_frame, text="")
        self.selected_directory_label_input.grid(row=1, column=2, sticky=tk.W)

        # Select Output Directory label and button
        self.select_output_label = tk.Label(self.widget_frame, text="Choose directory for saving:", font=("Calibri", 10, "bold"))
        self.select_output_label.grid(row=2, column=0, sticky=tk.W)
        self.select_dir_button_output = tk.Button(self.widget_frame, text="Choose directory", command=self.select_directory_output, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_output.grid(row=2, column=1, sticky=tk.W)
        self.selected_directory_label_output = tk.Label(self.widget_frame, text="")
        self.selected_directory_label_output.grid(row=2, column=2, sticky=tk.W)

        # Select Property label and menu
        self.property_label = tk.Label(self.widget_frame, text="Select Property:", font=("Calibri", 10, "bold"))
        self.property_label.grid(row=3, column=0, sticky=tk.W)
        self.selected_property = tk.StringVar(master)
        self.selected_property.set("Alpha")  # Default value

        # Create OptionMenu
        self.property_menu = tk.OptionMenu(self.widget_frame, self.selected_property, "Alpha", "Beta","Gamma", "Electric Dipole", command=self.on_property_select)
        self.property_menu.config(bg='#B4ADEA')
        self.property_menu.grid(row=3, column=1, sticky=tk.W)

        # Checkbuttons
        self.checkbutton1_value = tk.BooleanVar()
        self.checkbutton1 = tk.Checkbutton(self.widget_frame,text="Beta(0;0,0)", variable=self.checkbutton1_value)
        self.checkbutton2_value = tk.BooleanVar()
        self.checkbutton2 = tk.Checkbutton(self.widget_frame,text="Beta(-2w;w,w)", variable=self.checkbutton2_value)
        self.checkbutton3_value = tk.BooleanVar()
        self.checkbutton3 = tk.Checkbutton(self.widget_frame,text="Beta(-w;w,0)", variable=self.checkbutton3_value)

        # Create a frame to contain the buttons
        self.button_frame = tk.Frame(self.widget_frame)
        self.button_frame.grid(row=5, column=0, columnspan=4, pady=10)

        # Generate CSV file button
        self.run_button = tk.Button(self.button_frame, text="Generate CSV file", command=self.run_application, padx=20, pady=6, font=("Calibri", 10), fg="white", bg='#011627')
        self.run_button.pack(side=tk.LEFT, padx=10)

        # Exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.widget_frame.quit, font=("Calibri", 10), fg='#011627', width=5, highlightcolor="#011627", highlightthickness=2, highlightbackground='#011627')
        self.exit_button.pack(side=tk.RIGHT, padx=10)


        # Label to display messages
        self.message_label = tk.Label(self.widget_frame, text="")
        self.message_label.grid(row=6, columnspan=3)