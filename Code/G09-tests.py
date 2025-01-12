import tkinter as tk  
from tkinter import filedialog  
import os  
import csv  

# Import specific functions
from Backend.NLO_Functions import collect_limits, collect, read_file, calc, AlphaStatic, Alphaww, BetaStaticTot, BetaPockelsTot, BetaEFISHTot, BetaHRSCase, EletricDipoleTot, Gamma0000, Gammaww00, Gamma2www0, read_file_append, collect_09_A02
# File path and version for testing
log_file_path = "/home/florincy/NLO/Dados/pna_gaussian/g09-A02/pNA_g09-A02_gama.log"
version = "g09-A02"

# Read and process the log file
with open(log_file_path, "r") as log_file:
    if version == "g09-A02":
        unit = 1  # Unit for calculations for A02, that version prints only one unit
        start_line = collect_limits(log_file)[0]
        end_line = start_line + 16
        lines = read_file_append(log_file_path, start_line, end_line)
        print(lines)  # Debugging
        values = collect_09_A02(lines)
        print(values)  # Debugging
        print(EletricDipoleTot(values, "nan", unit))
        print(Alphaww(values,"nan",unit))

            
        
