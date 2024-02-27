#NLO Data Application
The NLO (Nonlinear Optics) Data Application is a Python GUI (Graphical User Interface) tool developed for processing and analyzing data from NLO calculations stored in .log files genereted by Gaussian program. This application allows users to select directories containing .log files, choose specific properties of interest, and generate CSV files for further analysis.

##Features
-Select directories containing .log files genereted from Gaussian calculations.
-Choose properties such as Alpha, Beta, Gamma, or Electric Dipole.
-Generate CSV files containing processed data.
-Provides a user-friendly interface for easy data processing.

###Units
    1.(au): Atomic units  
    2.(10**-30 esu): Electrostatic units (When this software calls esu, it is an abreviation to this full expression)
    3.(10**-50 SI): Système International (When this software calls SI, it is an abreviation to this full expression)
    4. (Debye): 10**-18 statcoulomb cm 

###Properties
    Alpha:
    The polarizability can be obteined from the alpha vector, in different units, by computing its norm.
    Beta:
    The hiperpolarizability can be obtained from the beta vector, in different units and in different conventions. The 2 possible conventions are based on Taylor series expansion (convertion "t") and on Perturbation series (convention "b"). Besides that, there are 3 possible response generators, simulating the possible experimental methodologies, which produce: Static Hiperpolarizability, HRS Hiperpolarizability and EFISH Hiperpolarizability.


#Installation 

'''
git clone https://github.com/florincy/NLO.git
'''

#Install the required dependencies:

'''
pip install -r math
'''
##Usage
Run the application by executing the following command:

'''
python main.py
'''

1. Select directories containing .log files for input 

2. Select the directory where you want the .csv output files to be saved.

3. Choose the desired property from the dropdown menu.

4. Click on the "Generate CSV file" button to process the data.

5. Click on the "Exit" button for ending the application

**The application will generate CSV files for each selected property, containing the processed data, in the output directory.**

##Dependencies
-Python 3.x
-tkinter
-NLO_Functions (custom module for processing NLO data)

##Contributing
Contributions are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue or submit a pull request.

##Citation
If you utilize this application in your work, we kindly request that you acknowledge it by citing:



