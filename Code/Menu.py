import tkinter as tk
from tkinter import filedialog
import os
import csv
from NLO_Functions import collect_limits, collect, read_file, calc, AlphaStatic, Alphaww, BetaStaticTot, BetaPockelsTot, BetaEFISHTot, BetaHRSCase, EletricDipoleTot, Gamma0000, Gammaww00, Gamma2www0

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO data app")
        self.main_frame = tk.Frame(master)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(self.main_frame)
        self.widget_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        # NLO data app label
        self.msg = tk.Label(self.main_frame, text="NLO Data Analysis", font=("Calibri", 20, "italic"))
        self.msg.grid(row=0, column=0)

        # Create a frame to contain the selectors
        self.selectors_frame = tk.Frame(self.widget_frame)
        self.selectors_frame.grid(row=2, column=0, columnspan=10, sticky="nsew")

        # Select Input Directory label and button
        self.select_input_label = tk.Label(self.selectors_frame, text="Choose .log files directory:", font=("Calibri", 14))
        self.select_input_label.grid(row=0, column=0, sticky=tk.W)
        self.select_dir_button_input = tk.Button(self.selectors_frame, text="Choose directory", command=self.select_directory_input, bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.select_dir_button_input.grid(row=0, column=1, sticky=tk.W)
        self.selected_directory_label_input = tk.Label(self.selectors_frame, text="")
        self.selected_directory_label_input.grid(row=1, column=0, columnspan=2, sticky=tk.W)

        # Select Output Directory label and button
        self.select_output_label = tk.Label(self.selectors_frame, text="Choose directory for saving:", font=("Calibri", 14))
        self.select_output_label.grid(row=2, column=0, sticky=tk.W)
        self.select_dir_button_output = tk.Button(self.selectors_frame, text="Choose directory", command=self.select_directory_output, bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.select_dir_button_output.grid(row=2, column=1, sticky=tk.W)
        self.selected_directory_label_output = tk.Label(self.selectors_frame, text="")
        self.selected_directory_label_output.grid(row=3, column=0, columnspan=2, sticky=tk.W)

        # Create frame for orientation widget
        self.orientation_frame = tk.Frame(self.widget_frame)
        self.orientation_frame.grid(row=3, column=0, columnspan=12, pady=5, sticky="nsew")

        # Select Orientation OptionMenu
        self.selected_orientation = tk.StringVar(master)
        self.selected_orientation.set("Dipole Orientation")  # Default value
        self.orientation_label = tk.Label(self.orientation_frame, text="Choose Orientation:", font=("Calibri", 14))
        self.orientation_label.grid(row=0, column=0, sticky=tk.W)
        self.orientation_menu = tk.OptionMenu(self.orientation_frame, self.selected_orientation, "Input Orientation", "Dipole Orientation")
        self.orientation_menu.config(bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.orientation_menu.grid(row=0, column=1, sticky=tk.W)

        # Create frame for Radiobuttons and Units
        self.radioutton_frame = tk.Frame(self.widget_frame)
        self.radioutton_frame.grid(row=4, column=0, columnspan=10, pady=5, sticky="nsew")

        # Select Units Label
        self.property_label = tk.Label(self.radioutton_frame, text="Choose Units:", font=("Calibri", 14))
        self.property_label.grid(row=0, column=3, sticky=tk.W)

        # Select units - Radiobuttons
        self.radiobutton1_units_value = tk.StringVar()
        self.radiobutton1_units = tk.Radiobutton(self.radioutton_frame, text="au", variable=self.radiobutton1_units_value, value="au", font=("Calibri", 12))
        self.radiobutton1_units.grid(row=0, column=4)

        self.radiobutton2_units_value = tk.StringVar()
        self.radiobutton2_units = tk.Radiobutton(self.radioutton_frame, text="Standard (esu/Debye)", variable=self.radiobutton1_units_value, value="standard", font=("Calibri", 12))
        self.radiobutton2_units.grid(row=0, column=5)

        self.radiobutton3_units_value = tk.StringVar()
        self.radiobutton3_units = tk.Radiobutton(self.radioutton_frame, text="SI", variable=self.radiobutton1_units_value, value="SI", font=("Calibri", 12))
        self.radiobutton3_units.grid(row=0, column=6)

        # Select Convention label
        self.property_label = tk.Label(self.radioutton_frame, text="Choose Convention:", font=("Calibri", 14))
        self.property_label.grid(row=0, column=0)

        # Select convention - Radiobuttons
        self.radiobutton1_value = tk.StringVar()
        self.radiobutton1 = tk.Radiobutton(self.radioutton_frame, text="T", variable=self.radiobutton1_value, value="T", font=("Calibri", 12))
        self.radiobutton1.grid(row=0, column=1)

        self.radiobutton2_value = tk.StringVar()
        self.radiobutton2 = tk.Radiobutton(self.radioutton_frame, text="B", variable=self.radiobutton1_value, value="B", font=("Calibri", 12))
        self.radiobutton2.grid(row=0, column=2)

        # Create a frame to contain the properties widgets
        self.property_frame = tk.Frame(self.widget_frame)
        self.property_frame.grid(row=5, column=0, columnspan=4, pady=7, sticky="nsew")

        # Select Property label and menu
        self.property_label = tk.Label(self.property_frame, text="Choose Property:", font=("Calibri", 14))
        self.property_label.grid(row=0, column=0, sticky=tk.W)
        self.selected_property = tk.StringVar(master)
        self.selected_property.set("Electric Dipole")  # Default value

        # Create OptionMenu
        self.property_menu = tk.OptionMenu(self.property_frame, self.selected_property, "Alpha", "Beta", "Gamma", "Electric Dipole", command=self.on_property_select)
        self.property_menu.config(bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.property_menu.grid(row=0, column=1, sticky=tk.W)

        # Create frame for Checkbuttons
        self.checkbutton_frame = tk.Frame(self.widget_frame)
        self.checkbutton_frame.grid(row=6, column=0, columnspan=4, pady=10, sticky="nsew") 

        # Checkbuttons for Properties
        self.checkbutton1_value = tk.BooleanVar()
        self.checkbutton1 = tk.Checkbutton(self.checkbutton_frame,text="Beta(0;0,0)", variable=self.checkbutton1_value, font=("Calibri", 12))

        self.checkbutton20_value = tk.BooleanVar()
        self.checkbutton20 = tk.Checkbutton(self.checkbutton_frame,text="Beta(-2w;w,w) EFISH", variable=self.checkbutton20_value, font=("Calibri", 12))

        self.checkbutton21_value = tk.BooleanVar()
        self.checkbutton21 = tk.Checkbutton(self.checkbutton_frame,text="Beta(-2w;w,w) HRS", variable=self.checkbutton21_value, font=("Calibri", 12))

        self.checkbutton3_value = tk.BooleanVar()
        self.checkbutton3 = tk.Checkbutton(self.checkbutton_frame,text="Beta(-w;w,0)", variable=self.checkbutton3_value, font=("Calibri", 12))

        self.checkbutton4_value = tk.BooleanVar()
        self.checkbutton4 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(0;0,0,0)", variable=self.checkbutton4_value, font=("Calibri", 12))

        self.checkbutton5_value = tk.BooleanVar()
        self.checkbutton5 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(-w;w,0,0)", variable=self.checkbutton5_value, font=("Calibri", 12))

        self.checkbutton6_value = tk.BooleanVar()
        self.checkbutton6 = tk.Checkbutton(self.checkbutton_frame,text="Gamma(-2w;w,w,0)", variable=self.checkbutton6_value, font=("Calibri", 12))

        self.checkbutton7_value = tk.BooleanVar()
        self.checkbutton7 = tk.Checkbutton(self.checkbutton_frame,text="Alpha(-w;w)", variable=self.checkbutton7_value, font=("Calibri", 12))

        self.checkbutton8_value = tk.BooleanVar()
        self.checkbutton8 = tk.Checkbutton(self.checkbutton_frame,text="Alpha(0;0)", variable=self.checkbutton8_value, font=("Calibri", 12))

        self.checkbutton9_value = tk.BooleanVar()
        self.checkbutton9 = tk.Checkbutton(self.main_frame,text="I want to see the components!", variable=self.checkbutton9_value, font=("Calibri", 12))
        self.checkbutton9.grid(row=7, column=0, sticky="nsew")    

        # Generate CSV file button
        self.run_button = tk.Button(self.main_frame, text="Generate CSV file", command=self.run_application, padx=20, pady=6, font=("Calibri", 14), fg="white", bg='#011627', relief='flat')
        self.run_button.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")

        # Label to display messages
        self.message_label = tk.Label(self.main_frame, text="")
        self.message_label.grid(row=9, column=0, columnspan=3, pady=5, sticky="nsew")


    def on_property_select(self, event):
        selected_property = self.selected_property.get()
        self.on_off_checkbox(selected_property)

    def on_off_checkbox(self, selected_property):
        if selected_property =="Beta":
            self.checkbutton1.grid(row=0, column=0, sticky=tk.W)
            self.checkbutton20.grid(row=0, column=1, sticky=tk.W)
            self.checkbutton21.grid(row=0, column=2, sticky=tk.W)
            self.checkbutton3.grid(row=0, column=3, sticky=tk.W)
            self.checkbutton5.grid_forget()
            self.checkbutton6.grid_forget()
            self.checkbutton7.grid_forget()
            self.checkbutton8.grid_forget()
        elif selected_property=="Gamma":
            self.checkbutton4.grid(row=0, column=0, sticky=tk.W)
            self.checkbutton5.grid(row=0, column=1, sticky=tk.W)
            self.checkbutton6.grid(row=0, column=2, sticky=tk.W)
            self.checkbutton1.grid_forget()
            self.checkbutton20.grid_forget()
            self.checkbutton21.grid_forget()
            self.checkbutton3.grid_forget()
            self.checkbutton7.grid_forget()
            self.checkbutton8.grid_forget()
        elif selected_property=="Alpha":
            self.checkbutton7.grid(row=0, column=0, sticky=tk.W)
            self.checkbutton8.grid(row=0, column=3, sticky=tk.W)
            self.checkbutton1.grid_forget()
            self.checkbutton20.grid_forget()
            self.checkbutton21.grid_forget()
            self.checkbutton3.grid_forget()
            self.checkbutton4.grid_forget()
            self.checkbutton5.grid_forget()
            self.checkbutton6.grid_forget()
        else:
            # Hide all checkbuttons if neither Beta nor Gamma is selected
            self.checkbutton1.grid_forget()
            self.checkbutton20.grid_forget()
            self.checkbutton21.grid_forget()
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
        components=self.checkbutton9_value.get()
        selected_property_value = self.selected_property.get()
        selected_orientation_value = self.selected_orientation.get()
        convention=self.radiobutton1_value.get()
        unit_button=self.radiobutton1_units_value.get()
        if unit_button=="au":
            unit=int(1)
        elif unit_button=="standard":
            unit=int(2)
        elif unit_button=="SI":
            unit=int(3)
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
                            returns=collect(file)
                            lines=returns[0]  
                            lines_beta_HRS=returns[1]  
                            for line in lines:
                                outputInput.write(line + "\n")
                    with open(outputDipolePath, "w") as outputDipole:
                        with open(output_file_path_dipole, "r") as file:
                            returns=collect(file)
                            lines=returns[0]  
                            lines_beta_HRS=returns[1]  
                            for line in lines:
                                outputDipole.write(line + "\n")
                    #Reading and dealing with resumed .txt files
                    if orientation=="Input Orientation":
                        with open(outputInputPath, "r") as file:
                            comment = "Input Orientation"
                            ret = calc(lines, name, comment)
                            #Dealing with HRS appart as it is a particular case
                            retHRS = calc(lines_beta_HRS, name, comment)
                            self.CSVoptions(option, directory_output, ret,retHRS, name,convention,unit,components)
                    elif orientation=="Dipole Orientation":
                        with open(outputDipolePath, "r") as file:
                            comment = "Dipole Orientation"
                            ret = calc(lines, name, comment)
                            #Dealing with HRS appart as it is a particular case
                            retHRS = calc(lines_beta_HRS, name, comment)
                            self.CSVoptions(option, directory_output, ret,retHRS,name,convention,unit,components)

    #Avaliates which .csv where requested and create them                   
    def CSVoptions(self, option, directory_output, ret,retHRS, name,convention,unit,components):
        if option == "Beta":
            checkbutton1_state = self.checkbutton1_value.get()
            checkbutton20_state = self.checkbutton20_value.get()
            checkbutton21_state = self.checkbutton21_value.get()
            checkbutton3_state = self.checkbutton3_value.get()

            if checkbutton1_state:
                output = os.path.join(directory_output, "BetaStatic.csv")
                betaStatic = BetaStaticTot(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaStatic)
            if checkbutton20_state:
                output = os.path.join(directory_output, "BetaEFISH.csv")
                betaEFISH = BetaEFISHTot(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaEFISH)
            if checkbutton21_state:
                output = os.path.join(directory_output, "BetaHRS.csv")
                betaHRS = BetaHRSCase(retHRS,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaHRS)
            if checkbutton3_state:
                output = os.path.join(directory_output, "BetaPockels.csv")
                betaPockels = BetaPockelsTot(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(betaPockels)
        elif option == "Gamma":
            checkbutton4_state = self.checkbutton4_value.get()
            checkbutton5_state = self.checkbutton5_value.get()
            checkbutton6_state = self.checkbutton6_value.get()

            if checkbutton4_state:
                output = os.path.join(directory_output, "Gamma0000.csv")
                gamma0000 = Gamma0000(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gamma0000)
            if checkbutton5_state:
                output = os.path.join(directory_output, "Gammaww00.csv")
                gammaww00 = Gammaww00(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gammaww00)
            if checkbutton6_state:
                output = os.path.join(directory_output, "Gamma2www0.csv")
                gamma2www0 = Gamma2www0(ret,name,convention,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(gamma2www0)
        elif option == "Alpha":
            checkbutton7_state = self.checkbutton7_value.get()
            checkbutton8_state = self.checkbutton8_value.get()

            if checkbutton7_state:
                output = os.path.join(directory_output, "AlphaStatic.csv")
                alphaStatic = AlphaStatic(ret,name,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(alphaStatic)
            if checkbutton8_state:
                output = os.path.join(directory_output, "Alphaww.csv")
                alphaww = Alphaww(ret,name,unit,components)
                with open(output, 'a', newline='') as df:
                    writer = csv.writer(df)
                    writer.writerows(alphaww)
        else:
            output = os.path.join(directory_output, f"{option}.csv")
            with open(output, 'a', newline='') as df:
                writer = csv.writer(df)
                dipole = EletricDipoleTot(ret,name,unit,components)
                writer.writerows(dipole)

        self.message_label.config(text=".csv file generated for " + option)

