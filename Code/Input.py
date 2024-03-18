import tkinter as tk
from tkinter import filedialog
from InputGenerator import generate_input_file
solvents = ['Water', 'Acetonitrile', 'Methanol', 'Ethanol', 'IsoQuinoline', 'Quinoline', 'Chloroform', 'DiethylEther', 'Dichloromethane', 'DiChloroEthane', 'CarbonTetraChloride', 'Benzene', 'Toluene', 'ChloroBenzene', 'NitroMethane', 'Heptane', 'CycloHexane', 'Aniline', 'Acetone', 'TetraHydroFuran', 'DiMethylSulfoxide', 'Argon', 'Krypton', 'Xenon', 'n-Octanol', '1,1,1-TriChloroEthane', '1,1,2-TriChloroEthane', '1,2,4-TriMethylBenzene', '1,2-DiBromoEthane', '1,2-EthaneDiol', '1,4-Dioxane', '1-Bromo-2-MethylPropane', '1-BromoOctane', '1-BromoPentane', '1-BromoPropane', '1-Butanol', '1-ChloroHexane', '1-ChloroPentane', '1-ChloroPropane', '1-Decanol', '1-FluoroOctane', '1-Heptanol', '1-Hexanol', '1-Hexene', '1-Hexyne', '1-IodoButane', '1-IodoHexaDecane', '1-IodoPentane', '1-IodoPropane', '1-NitroPropane', '1-Nonanol', '1-Pentanol', '1-Pentene', '1-Propanol', '2,2,2-TriFluoroEthanol', '2,2,4-TriMethylPentane', '2,4-DiMethylPentane', '2,4-DiMethylPyridine', '2,6-DiMethylPyridine', '2-BromoPropane', '2-Butanol', '2-ChloroButane', '2-Heptanone', '2-Hexanone', '2-MethoxyEthanol', '2-Methyl-1-Propanol', '2-Methyl-2-Propanol', '2-MethylPentane', '2-MethylPyridine', '2-NitroPropane', '2-Octanone', '2-Pentanone', '2-Propanol', '2-Propen-1-ol', '3-MethylPyridine', '3-Pentanone', '4-Heptanone', '4-Methyl-2-Pentanone', '4-MethylPyridine', '5-Nonanone', 'AceticAcid', 'AcetoPhenone', 'a-ChloroToluene', 'Anisole', 'Benzaldehyde', 'BenzoNitrile', 'BenzylAlcohol', 'BromoBenzene', 'BromoEthane', 'Bromoform', 'Butanal', 'ButanoicAcid', 'Butanone', 'ButanoNitrile', 'ButylAmine', 'ButylEthanoate', 'CarbonDiSulfide', 'Cis-1,2-DiMethylCycloHexane', 'Cis-Decalin', 'CycloHexanone', 'CycloPentane', 'CycloPentanol', 'CycloPentanone', 'Decalin-mixture', 'DiBromomEthane', 'DiButylEther', 'DiEthylAmine', 'DiEthylSulfide', 'DiIodoMethane', 'DiIsoPropylEther', 'DiMethylDiSulfide', 'DiPhenylEther', 'DiPropylAmine', 'e-1,2-DiChloroEthene', 'e-2-Pentene', 'EthaneThiol', 'EthylBenzene', 'EthylEthanoate', 'EthylMethanoate', 'EthylPhenylEther', 'FluoroBenzene', 'Formamide', 'FormicAcid', 'HexanoicAcid', 'IodoBenzene', 'IodoEthane', 'IodoMethane', 'IsoPropylBenzene', 'm-Cresol', 'Mesitylene', 'MethylBenzoate', 'MethylButanoate', 'MethylCycloHexane', 'MethylEthanoate', 'MethylMethanoate', 'MethylPropanoate', 'm-Xylene', 'n-ButylBenzene', 'n-Decane', 'n-Dodecane', 'n-Hexadecane', 'n-Hexane', 'NitroBenzene', 'NitroEthane', 'n-MethylAniline', 'n-MethylFormamide-mixture', 'n,n-DiMethylAcetamide', 'n,n-DiMethylFormamide', 'n-Nonane', 'n-Octane', 'n-Pentadecane', 'n-Pentane', 'n-Undecane', 'o-ChloroToluene', 'o-Cresol', 'o-DiChloroBenzene', 'o-NitroToluene', 'o-Xylene', 'Pentanal', 'PentanoicAcid', 'PentylAmine', 'PentylEthanoate', 'PerFluoroBenzene', 'p-IsoPropylToluene', 'Propanal', 'PropanoicAcid', 'PropanoNitrile', 'PropylAmine', 'PropylEthanoate', 'p-Xylene', 'Pyridine', 'sec-ButylBenzene', 'tert-ButylBenzene', 'TetraChloroEthene', 'TetraHydroThiophene-s,s-dioxide', 'Tetralin', 'Thiophene', 'Thiophenol', 'trans-Decalin', 'TriButylPhosphate', 'TriChloroEthene', 'TriEthylAmine', 'Xylene-mixture', 'z-1,2-DiChloroEthene']
functionals = ['B3LYP', 'B3P86', 'O3LYP', 'APFD', 'wB97XD', 'LC-wHPBE', 'LC-wPBE', 'CAM-B3LYP', 'wB97', 'wB97X', 'LC-BLYP', 'MN15', 'M11', 'SOGGA11X', 'N12SX', 'MN12SX', 'PW6B95', 'PW6B95D3', 'M08HX', 'M06', 'M06HF', 'M062X', 'PBE1PBE', 'HSEH1PBE', 'OHSE2PBE', 'OHSE1PBE', 'PBEh1PBE', 'B1B95', 'B1LYP', 'mPW1PW91', 'mPW1LYP', 'mPW1PBE', 'mPW3PBE', 'B98', 'B971', 'B972', 'TPSSh', 'tHCTHhyb', 'BMK', 'HISSbPBE', 'X3LYP', 'BHandH', 'BHandHLYP']
#INITAL SETTINGS AND FRAMES --------------------------------------------------------------------------------
class FormPreviewApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Form and Preview")
        #Main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        # Initialize Tkinter variables
        self.filepath="none"
        self.charge_input_var = tk.StringVar()
        self.multi_input_var = tk.StringVar()
        self.freq_input_var = tk.StringVar()
        self.selected_directory_path = ""
        self.input = ""

        # Create frames for form and preview
        self.form_frame = tk.Frame(self.main_frame)
        self.form_frame.grid(row=0, column=0, sticky="nsew")
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_rowconfigure(0, weight=1)

        self.preview_frame = tk.Frame(self.main_frame, bg="lightgray")
        self.preview_frame.grid(row=0, column=1, sticky="nsew")
        self.preview_frame.grid_columnconfigure(0, weight=1)
        self.preview_frame.grid_rowconfigure(0, weight=1)

        # Create form elements
        self.create_form()

        # Create preview elements
        self.create_preview()

        # Bind events to form elements
        self.bind_events()

#EVENTS AND BACK INTEGRATION --------------------------------------------------------------------------------
    def bind_events(self):
        # Bind events to form elements
        self.freq_input_entry.bind("<FocusOut>", self.update_preview)
        self.multi_input_entry.bind("<FocusOut>", self.update_preview)
        self.charge_input_entry.bind("<FocusOut>", self.update_preview)
        self.functional_listbox.bind("<ButtonRelease-1>", self.update_preview)
        self.basis_listbox.bind("<ButtonRelease-1>", self.update_preview)
        self.solvent_listbox.bind("<ButtonRelease-1>", self.update_preview)
        #for checkbutton in self.checkbox_buttons:
         #   checkbutton.bind("<ButtonRelease-1>", self.update_preview)

    def update_preview(self, event=None):
        # Update the preview with the current form values
        functional_index = self.functional_listbox.curselection()
        solvent_index = self.solvent_listbox.curselection()
        basis_index = self.basis_listbox.curselection()
        functional = self.functional_listbox.get(functional_index[0]) if functional_index else ""
        solvent = self.solvent_listbox.get(solvent_index[0]) if solvent_index else ""
        basis = self.basis_listbox.get(basis_index[0]) if basis_index else ""
        charge = self.charge_input_var.get()
        multi = self.multi_input_var.get()
        freq = self.freq_input_var.get()
        checkbox_values = [var.get() for var in self.checkbox_vars]
        property = ""
        if (checkbox_values[0] == True or checkbox_values[1]) and checkbox_values[2]==False and checkbox_values[3]==False :
            property += "Dipole"
        elif checkbox_values[2]==True and checkbox_values[3]==True:
            property += "Cubic,Four,DCSHG"
        elif checkbox_values[2]==True and checkbox_values[3]==False:
            property += "Cubic,DCSHG"
        elif checkbox_values[2]==False and checkbox_values[3]==True:
            property += "Four,DCSHG"
        print(property)
        directory = self.selected_directory_path
        filepath = self.filepath
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    filelist = file.read().splitlines()[1:]
                    # Read content and exclude the first line
            except FileNotFoundError:
                print("File not found.")
                return
            print(filelist)
            self.input = generate_input_file("chk_file", "4000", "2", functional, solvent, charge, multi, filelist, freq, property,basis)
            self.preview_text.delete(1.0, tk.END)  # Clear previous content
            self.preview_text.insert(tk.END, self.input)
                
    def create_preview(self):
        # Add preview elements
        self.preview_label = tk.Label(self.preview_frame, text="Preview", font=("Calibri", 14), bg="lightgray")
        self.preview_label.pack(expand=False)

        self.preview_text = tk.Text(self.preview_frame, font=("Calibri", 9), wrap=tk.WORD, width=45, height=20)  # Adjust the width and height as needed
        self.preview_text.pack(expand=True, fill=tk.BOTH)

        # Update the preview initially
        self.update_preview()

    def write_input(self):
        if self.input:
            inputpath= self.selected_directory_path + "/NLO-input.com"
            with open(inputpath, 'w') as file:
                file.writelines(self.input)

#FILE DIALOGS EVENT ---------------------------------------------------------------------------------------
    def select_directory_input(self):
        # Prompt the user to select a directory
        directory = filedialog.askdirectory()
        
        # If a directory is selected, store the path and update the label
        if directory:
            self.selected_directory_path = directory
            self.selected_directory_label_input.config(text=directory)
    def select_xyz_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("XYZ Files", "*.xyz")])
        if filepath:
            self.filepath = filepath  # Store the file path
            with open(filepath, 'r') as file:
                filelist = file.read().splitlines()[1:]  # Read content and exclude the first line
                content = '\n'.join(filelist)  # Rejoin the lines into a single string
                #self.preview_text.delete(1.0, tk.END)  # Clear previous content
                #self.preview_text.insert(tk.END, content)
                self.update_preview()
#-----------------------------------------------------------------------------------------------------------


#FRONT DESIGN ----------------------------------------------------------------------------------------------
    def create_form(self):
        # Add form elements
        tk.Label(self.form_frame, text="Choose directory to save it:", font=("Calibri", 14)).grid(row=0, column=0, sticky=tk.W)
        self.select_dir_button_input = tk.Button(self.form_frame, text="Choose directory", command=self.select_directory_input, bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.select_dir_button_input.grid(row=0, column=1)
        self.selected_directory_label_input = tk.Label(self.form_frame, text="")
        self.selected_directory_label_input.grid(row=1, column=0)

        tk.Label(self.form_frame, text="Choose XYZ file:", font=("Calibri", 14)).grid(row=2, column=0, sticky=tk.W)
        self.select_xyz_button = tk.Button(self.form_frame, text="Select XYZ file", command=self.select_xyz_file, bg='#7C98B3', font=("Calibri", 12), relief='flat')
        self.select_xyz_button.grid(row=2, column=1,pady=5)

        # Add selectors
        tk.Label(self.form_frame, text="Functional:", font=("Calibri", 14)).grid(row=3, column=0, sticky=tk.W)
        self.functional_var = tk.StringVar()
        self.functional_var.set("CAM-B3LYP")
        self.functional_listbox = tk.Listbox(self.form_frame, listvariable=self.functional_var, font=("Calibri", 12), relief='flat', selectmode=tk.SINGLE, exportselection=0, height=3)
        self.functional_listbox.grid(row=3, column=1, sticky="ew")
        for option in functionals:
            self.functional_listbox.insert(tk.END, option)

        tk.Label(self.form_frame, text="Basis set:", font=("Calibri", 14)).grid(row=4, column=0, sticky=tk.W)
        self.basis_var = tk.StringVar()
        self.basis_var.set("631-G")
        self.basis_listbox = tk.Listbox(self.form_frame, listvariable=self.basis_var, font=("Calibri", 12), relief='flat', selectmode=tk.SINGLE, exportselection=0, height=3)
        self.basis_listbox.grid(row=4, column=1, sticky="ew")
        self.basis_listbox.insert(tk.END, "NLO-I", "NLO-II", "NLO-III")

        # Add scrollbars
        self.functional_scrollbar = tk.Scrollbar(self.form_frame, command=self.functional_listbox.yview)
        self.functional_scrollbar.grid(row=3, column=2, sticky="ns")
        self.functional_listbox.config(yscrollcommand=self.functional_scrollbar.set)

        self.basis_scrollbar = tk.Scrollbar(self.form_frame, command=self.basis_listbox.yview)
        self.basis_scrollbar.grid(row=4, column=2, sticky="ns")
        self.basis_listbox.config(yscrollcommand=self.basis_scrollbar.set)

        # Add additional selector
        tk.Label(self.form_frame, text="Select Solvent:", font=("Calibri", 14)).grid(row=5, column=0, sticky=tk.W)
        self.solvent_var = tk.StringVar()
        self.solvent_var.set("None")
        self.solvent_listbox = tk.Listbox(self.form_frame, listvariable=self.solvent_var, font=("Calibri", 12), relief='flat', selectmode=tk.SINGLE, exportselection=0, height=3)
        self.solvent_listbox.grid(row=5, column=1, sticky="ew")
        for option in solvents:
            self.solvent_listbox.insert(tk.END, option)

        # Add scrollbar for Option 3 listbox
        self.solvent_scrollbar = tk.Scrollbar(self.form_frame, command=self.solvent_listbox.yview)
        self.solvent_scrollbar.grid(row=5, column=2, sticky="ns")
        self.solvent_listbox.config(yscrollcommand=self.solvent_scrollbar.set)

        # Add checkboxes with four options
        tk.Label(self.form_frame, text="Select Properties:", font=("Calibri", 14)).grid(row=6, column=0, sticky=tk.W)
        self.checkbox_vars = [tk.BooleanVar() for i in range(4)]
        self.checkbox_options = ["Electric Dipole", "Alpha", "Beta", "Gamma"]
        for i, option in enumerate(self.checkbox_options):
            tk.Checkbutton(self.form_frame, text=option, variable=self.checkbox_vars[i], font=("Calibri", 12)).grid(row=6+i, column=1, sticky=tk.W)
        
        # Add text input
        tk.Label(self.form_frame, text="Laser Frequency:", font=("Calibri", 14)).grid(row=11, column=0, sticky=tk.W)
        self.freq_input_var = tk.StringVar()
        self.freq_input_entry = tk.Entry(self.form_frame, textvariable=self.freq_input_var, font=("Calibri", 12), relief='flat')
        self.freq_input_entry.grid(row=11, column=1, sticky="ew")

        # Add text input
        tk.Label(self.form_frame, text="Multiplicity:", font=("Calibri", 14)).grid(row=12, column=0, sticky=tk.W)
        self.multi_input_var = tk.StringVar()
        self.multi_input_entry = tk.Entry(self.form_frame, textvariable=self.multi_input_var, font=("Calibri", 12), relief='flat')
        self.multi_input_entry.grid(row=12, column=1, sticky="ew")
        # Add text input
        tk.Label(self.form_frame, text="Charge:", font=("Calibri", 14)).grid(row=13, column=0, sticky=tk.W)
        self.charge_input_var = tk.StringVar()
        self.charge_input_entry = tk.Entry(self.form_frame, textvariable=self.charge_input_var, font=("Calibri", 12), relief='flat')
        self.charge_input_entry.grid(row=13, column=1, sticky="ew")
        #Add button
        write_button = tk.Button(self.main_frame, text="Write File", command=self.write_input, relief='flat',font=("Calibri", 14), fg="white", bg='#011627')
        write_button.grid(row=14, column=0,columnspan=2,pady=5)


