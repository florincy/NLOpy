import tkinter as tk
from tkinter import filedialog
import os
import csv
from NLO_Functions import collect_limits, collect, read_file, calc, AlphaStatic,Alphaww, BetaStaticTot, BetaHRSTot, BetaEFISHTot, EletricDipoleTot, Gamma0000,Gammaww00, Gamma2www0
from Application import Application

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

        # Create a frame to contain the selectors
        self.selectors_frame = tk.Frame(self.widget_frame)
        self.selectors_frame.grid(column=0, columnspan=4)

        # Select Input Directory label and button
        self.select_input_label = tk.Label(self.selectors_frame, text="Choose .log files directory:", font=("Calibri", 10, "bold"))
        self.select_input_label.grid(row=1, column=0, columnspan=2, sticky=tk.W)
        self.select_dir_button_input = tk.Button(self.selectors_frame, text="Choose directory", command=self.select_directory_input, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_input.grid(row=1, column=2, sticky=tk.W)
        self.selected_directory_label_input = tk.Label(self.selectors_frame, text="")
        self.selected_directory_label_input.grid(row=2, column=0, columnspan=4, sticky=tk.W)

        # Select Output Directory label and button
        self.select_output_label = tk.Label(self.selectors_frame, text="Choose directory for saving:", font=("Calibri", 10, "bold"))
        self.select_output_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)
        self.select_dir_button_output = tk.Button(self.selectors_frame, text="Choose directory", command=self.select_directory_output, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_output.grid(row=3, column=2, sticky=tk.W)
        self.selected_directory_label_output = tk.Label(self.selectors_frame, text="")
        self.selected_directory_label_output.grid(row=4, column=0, columnspan=4, sticky=tk.W)

        # Create frame for Radiobuttons and Orientations
        self.radioutton_frame = tk.Frame(self.widget_frame)
        self.radioutton_frame.grid(row=4, column=0, columnspan=4)


        # Select Orientation label
        self.property_label = tk.Label(self.radioutton_frame, text="Select Convention:", font=("Calibri", 10, "bold"))
        self.property_label.grid(row=0, column=0, sticky=tk.W)

        # Select convention - Radiobuttons
        self.radiobutton1_value = tk.StringVar()
        self.radiobutton1 = tk.Radiobutton(self.radioutton_frame, text="T", variable=self.radiobutton1_value, value="T")
        self.radiobutton1.grid(row=0, column=1, sticky=tk.W)

        self.radiobutton2_value = tk.StringVar()
        self.radiobutton2 = tk.Radiobutton(self.radioutton_frame, text="B", variable=self.radiobutton1_value, value="B")
        self.radiobutton2.grid(row=0, column=2, sticky=tk.W)

        # Select Orientation OptionMenu
        self.selected_orientation = tk.StringVar(master)
        self.selected_orientation.set("Dipole Orientation")  # Default value
        self.orientation_label = tk.Label(self.radioutton_frame, text="Select Orientation:", font=("Calibri", 10,"bold"))
        self.orientation_label.grid(row=0, column=3, sticky=tk.W)
        self.orientation_menu = tk.OptionMenu(self.radioutton_frame, self.selected_orientation, "Input Orientation", "Dipole Orientation")
        self.orientation_menu.config(bg='#B4ADEA')
        self.orientation_menu.grid(row=0, column=4, sticky=tk.W)
        
        # Create a frame to contain the properties widgets
        self.property_frame = tk.Frame(self.widget_frame)
        self.property_frame.grid(row=7,column=0, columnspan=4,pady=6)

        # Select Property label and menu
        self.property_label = tk.Label(self.property_frame, text="Select Property:", font=("Calibri", 10, "bold"))
        self.property_label.grid(row=7,column=0, sticky=tk.W)
        self.selected_property = tk.StringVar(master)
        self.selected_property.set("Electric Dipole")  # Default value

        # Create OptionMenu
        self.property_menu = tk.OptionMenu(self.property_frame, self.selected_property, "Alpha", "Beta","Gamma", "Electric Dipole", command=self.on_property_select)
        self.property_menu.config(bg='#B4ADEA')
        self.property_menu.grid(row=7,column=2, sticky=tk.W)

        # Create frame for Checkbuttons
        self.checkbutton_frame = tk.Frame(self.widget_frame)
        self.checkbutton_frame.grid(row=8, column=0, columnspan=4, pady=10) 

        # Checkbuttons
        self.checkbutton1_value = tk.BooleanVar()
        self.checkbutton1 = tk.Checkbutton(self.checkbutton_frame,text="Beta(0;0,0)", variable=self.checkbutton1_value)
        self.checkbutton2_value = tk.BooleanVar()
        self.checkbutton2 = tk.Checkbutton(self.checkbutton_frame,text="Beta(-2w;w,w)", variable=self.checkbutton2_value)
        self.checkbutton3_value = tk.BooleanVar()
        self.checkbutton3 = tk.Checkbutton(self.checkbutton_frame,text="Beta(-w;w,0)", variable=self.checkbutton3_value)

        # Checkbuttons
        self.checkbutton4_value = tk.BooleanVar()
        self.checkbutton4 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(0;0,0,0)", variable=self.checkbutton4_value)
        self.checkbutton5_value = tk.BooleanVar()
        self.checkbutton5 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(-w;w,0,0)", variable=self.checkbutton5_value)
        self.checkbutton6_value = tk.BooleanVar()
        self.checkbutton6 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(-2w;w,w,0)", variable=self.checkbutton6_value)

        # Checkbuttons 
        self.checkbutton7_value = tk.BooleanVar()
        self.checkbutton7 = tk.Checkbutton(self.checkbutton_frame,text="Alpha(-w;w)", variable=self.checkbutton7_value)
        self.checkbutton8_value = tk.BooleanVar()
        self.checkbutton8 = tk.Checkbutton(self.checkbutton_frame,text="Alpha(0;0)", variable=self.checkbutton8_value)

        # Create a frame to contain the buttons
        self.button_frame = tk.Frame(self.widget_frame)
        self.button_frame.grid(row=9, column=0, columnspan=4, pady=10)         

        # Generate CSV file button
        self.run_button = tk.Button(self.button_frame, text="Generate CSV file", command=self.run_application, padx=20, pady=6, font=("Calibri", 10), fg="white", bg='#011627')
        self.run_button.pack(side=tk.LEFT, padx=10)

        # Exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.widget_frame.quit, font=("Calibri", 10), fg='#011627', width=5, highlightcolor="#011627", highlightthickness=2, highlightbackground='#011627')
        self.exit_button.pack(side=tk.RIGHT, padx=10)


        # Label to display messages
        self.message_label = tk.Label(self.widget_frame, text="")
        self.message_label.grid(row=10, columnspan=3)

    def on_property_select(self, event):
        selected_property = self.selected_property.get()
        self.on_off_checkbox(selected_property)

    def on_off_checkbox(self, selected_property):
        if selected_property =="Beta":
            self.checkbutton1.grid(row=5, column=0, sticky=tk.W)
            self.checkbutton2.grid(row=5, column=1, sticky=tk.W)
            self.checkbutton3.grid(row=5, column=2, sticky=tk.W)
            self.checkbutton4.grid_forget()
            self.checkbutton5.grid_forget()
            self.checkbutton6.grid_forget()
            self.checkbutton7.grid_forget()
            self.checkbutton8.grid_forget()
        elif selected_property=="Gamma":
            self.checkbutton4.grid(row=5, column=0, sticky=tk.W)
            self.checkbutton5.grid(row=5, column=1, sticky=tk.W)
            self.checkbutton6.grid(row=5, column=2, sticky=tk.W)
            self.checkbutton1.grid_forget()
            self.checkbutton2.grid_forget()
            self.checkbutton3.grid_forget()
            self.checkbutton7.grid_forget()
            self.checkbutton8.grid_forget()
        elif selected_property=="Alpha":
            self.checkbutton7.grid(row=5, column=0, sticky=tk.W)
            self.checkbutton8.grid(row=5, column=2, sticky=tk.W)
            self.checkbutton1.grid_forget()
            self.checkbutton2.grid_forget()
            self.checkbutton3.grid_forget()
            self.checkbutton4.grid_forget()
            self.checkbutton5.grid_forget()
            self.checkbutton6.grid_forget()
        else:
            # Hide all checkbuttons if neither Beta nor Gamma is selected
            self.checkbutton1.grid_forget()
            self.checkbutton2.grid_forget()
            self.checkbutton3.grid_forget()
            self.checkbutton4.grid_forget()
            self.checkbutton5.grid_forget()
            self.checkbutton6.grid_forget()
            self.checkbutton7.grid_forget()
            self.checkbutton8.grid_forget()

    def select_directory_input(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory_label_input.config(text="Selected Input Directory: " + directory)
            self.selected_directory_input = directory 

    def select_directory_output(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_directory_label_output.config(text="Selected Output Directory: " + directory)
            self.selected_directory_output = directory 

    def run_application(self):
        selected_property_value = self.selected_property.get()
        selected_orientation_value = self.selected_orientation.get()
        convention=self.radiobutton1_value.get()
        print(convention)
        option = selected_property_value
        orientation=selected_orientation_value
        if not hasattr(self, 'selected_directory_input') or not hasattr(self, 'selected_directory_output'):
            self.message_label["text"] = "Error: Please select both input and output directories."
            return

        directory_input = self.selected_directory_input
        directory_output = self.selected_directory_output
        print("Running application")  

        for path, dirs, files in os.walk(directory_input):
            for name in files:
                if name.endswith(".log"):
                    log_file_path = os.path.join(path, name)
                    print(f"Processing file: {log_file_path}")

                    returns = collect_limits(open(log_file_path, "r"))
                    line1, line2 = returns[0], returns[1]
                    input_ref = read_file(log_file_path, line1, line2)
                    input_dip = read_file(log_file_path, line2)

                    output_file_path_dipole = os.path.join(path, "DipoleReference.txt")
                    output_file_path_input = os.path.join(path, "InputReference.txt")

                    with open(output_file_path_dipole, "w") as output_file:
                        for line in input_dip:
                            output_file.write(line + "\n")
                    with open(output_file_path_input, "w") as output_file:
                        for line in input_ref:
                            output_file.write(line + "\n")
                    outputInputPath = os.path.join(directory_output, "ResultInp.txt")
                    outputDipolePath = os.path.join(directory_output, "ResultDip.txt")
                    #Writing resumed .txt files
                    with open(outputInputPath, "w") as outputInput:
                        with open(output_file_path_input, "r") as file:
                            lines = collect(file)
                            for line in lines:
                                outputInput.write(line + "\n")
                    with open(outputDipolePath, "w") as outputDipole:
                        with open(output_file_path_dipole, "r") as file:
                            lines = collect(file)
                            for line in lines:
                                outputDipole.write(line + "\n")
                    #Reading and dealing with resumed .txt files
                    if orientation=="Input Orientation":
                        with open(outputInputPath, "r") as file:
                            comment = "Input Orientation"
                            ret = calc(file, name, comment)
                            self.CSVoptions(option, directory_output, ret, name,convention)
                    elif orientation=="Dipole Orientation":
                        with open(outputDipolePath, "r") as file:
                            comment = "Dipole Orientation"
                            ret = calc(file, name, comment)
                            self.CSVoptions(option, directory_output, ret, name,convention)

    #Avaliates which .csv where requested and create them                   
    def CSVoptions(self, option, directory_output, ret, name,convention):
        if option == "Beta":
            checkbutton1_state = self.checkbutton1_value.get()
            checkbutton2_state = self.checkbutton2_value.get()
            checkbutton3_state = self.checkbutton3_value.get()

            if checkbutton1_state:
                output = os.path.join(directory_output, "BetaStatic.csv")
                betaStatic = BetaStaticTot(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaStatic)
            if checkbutton2_state:
                output = os.path.join(directory_output, "BetaHRS.csv")
                betaHRS = BetaHRSTot(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaHRS)
            if checkbutton3_state:
                output = os.path.join(directory_output, "BetaEFISH.csv")
                betaEFISH = BetaEFISHTot(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaEFISH)

        elif option == "Gamma":
            checkbutton4_state = self.checkbutton4_value.get()
            checkbutton5_state = self.checkbutton5_value.get()
            checkbutton6_state = self.checkbutton6_value.get()

            if checkbutton4_state:
                output = os.path.join(directory_output, "GammaStatic.csv")
                gamma = Gamma0000(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gamma)
            if checkbutton5_state:
                output = os.path.join(directory_output, "GammaKerreffect.csv")
                gamma = Gammaww00(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gamma)
            if checkbutton6_state:
                output = os.path.join(directory_output, "GammaEFISH.csv")
                gamma = Gamma2www0(ret, name,convention)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gamma)
        
        elif option == "Alpha":
            checkbutton7_state = self.checkbutton7_value.get()
            checkbutton8_state = self.checkbutton8_value.get()

            if checkbutton7_state:
                output = os.path.join(directory_output, "AlphaStatic.csv")
                alpha = AlphaStatic(ret, name)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(alpha)
            if checkbutton8_state:
                output = os.path.join(directory_output, "AlphaEFISH.csv")
                alpha = Alphaww(ret, name)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(alpha)

        else:
            output = os.path.join(directory_output, f"{option}.csv")
            with open(output, 'a', newline='') as df:
                writer = csv.writer(df)
                dipole = EletricDipoleTot(ret, name)
                writer.writerows(dipole)

        self.message_label.config(text=".csv file generated for " + option)


root = tk.Tk()
app = Application(root)
root.mainloop()
