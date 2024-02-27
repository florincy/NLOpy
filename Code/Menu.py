import tkinter as tk
from tkinter import filedialog
import os
import csv
from NLO_Functions import collect_limits, collect, read_file, calc, AlphaTot, BetaTot, EletricDipoleTot, GammaTot

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO data app")
        
        # Create a frame to contain the widgets
        self.widget_frame = tk.Frame(master)
        self.widget_frame.pack(expand=True, fill=tk.BOTH)  # Expand to fill the available space
        
        # Centering the frame on the window
        self.widget_frame.grid_rowconfigure(0, weight=1)
        self.widget_frame.grid_columnconfigure(0, weight=1)

        # NLO data app label
        self.msg = tk.Label(self.widget_frame, text="NLO data app", font=("Calibri", 16, "italic", "bold"))
        self.msg.pack()

        # Select Property label
        self.property_label = tk.Label(self.widget_frame, text="Choose .log files directory:", font=("Calibri", 10, "bold"))
        self.property_label.pack()

        # Select Directory containing .log files button
        self.select_dir_button_input = tk.Button(self.widget_frame, text="Choose directory", command=self.select_directory_input, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_input.pack()

        # Label to display selected directory for input
        self.selected_directory_label_input = tk.Label(self.widget_frame, text="")
        self.selected_directory_label_input.pack()

        # Select Property label
        self.property_label = tk.Label(self.widget_frame, text="Choose directory for saving:", font=("Calibri", 10, "bold"))
        self.property_label.pack()

        # Select Directory for saving the .csv files button
        self.select_dir_button_output = tk.Button(self.widget_frame, text="Choose directory", command=self.select_directory_output, bg='#b4adea', font=("Calibri", 10))
        self.select_dir_button_output.pack()
        
        # Label to display selected directory for output
        self.selected_directory_label_output = tk.Label(self.widget_frame, text="")
        self.selected_directory_label_output.pack()

        # Select Property label
        self.property_label = tk.Label(self.widget_frame, text="Select Property:", font=("Calibri", 10, "bold"))
        self.property_label.pack()

        # Option menu for selecting property
        self.selected_property = tk.StringVar(master)
        self.selected_property.set("Alpha")  # Default value
        self.property_menu = tk.OptionMenu(self.widget_frame, self.selected_property, "Alpha", "Beta", "Gamma", "Electric Dipole")
        self.property_menu.config(bg='#B4ADEA')
        self.property_menu.pack(padx=10, pady=10)

        # Frame to contain the buttons
        self.button_frame = tk.Frame(self.widget_frame)
        self.button_frame.pack()

        # Generate CSV file button
        self.run_button = tk.Button(self.button_frame, text="Generate CSV file", command=self.run_application, padx=20, pady=6, font=("Calibri", 10), fg="white",bg='#011627')
        self.run_button.pack(side=tk.LEFT,padx=7)

        # Exit button
        self.sair = tk.Button(self.button_frame, text="Exit", command=self.widget_frame.quit, font=("Calibri", 10), fg='#011627', width=5,highlightcolor="#011627",highlightthickness=2,highlightbackground='#011627')
        self.sair.pack(side=tk.RIGHT, padx=7, pady=10)

        # Label to display messages
        self.mensagem = tk.Label(self.widget_frame, text="")
        self.mensagem.pack()

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
        print("Selected Property:", selected_property_value)
        option = selected_property_value

        if not hasattr(self, 'selected_directory_input') or not hasattr(self, 'selected_directory_output'):
            self.mensagem["text"] = "Error: Please select both input and output directories."
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

                    output = os.path.join(directory_output, f"{option}.csv")
                    print(output)
                    with open(output, 'a', newline='') as df:
                        writer = csv.writer(df)
                        with open(outputInputPath, "r") as file:
                            comment = "Input Orientation"
                            ret = calc(file, name, comment)
                            if option == "Alpha":
                                alpha = AlphaTot(ret, name)
                                writer.writerows(alpha)
                            elif option == "Beta":
                                beta = BetaTot(ret, name)
                                writer.writerows(beta)
                            elif option == "Gamma":
                                GammaTot(ret, name)
                            elif option == "Electric Dipole":
                                dipole = EletricDipoleTot(ret, name)
                                writer.writerows(dipole)
                            else:
                                print("Error")

                        with open(outputDipolePath, "r") as file:
                            comment = "Dipole Orientation"
                            ret = calc(file, name, comment)
                            if option == "Alpha":
                                alpha = AlphaTot(ret, name)
                                writer.writerows(alpha)
                            elif option == "Beta":
                                beta = BetaTot(ret, name)
                                writer.writerows(beta)
                            elif option == "Gamma":
                                GammaTot(ret, name)
                            elif option == "Electric Dipole":
                                dipole = EletricDipoleTot(ret, name)
                                writer.writerows(dipole)
                            else:
                                print("Error")   
                    self.mensagem["text"] = ".csv file generated for " + option

root = tk.Tk()
app = Application(root)
root.mainloop()

