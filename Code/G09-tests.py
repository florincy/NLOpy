import tkinter as tk
from tkinter import filedialog
import os
import csv
from Backend.NLO_Functions import collect_limits, collect, read_file, calc, AlphaStatic, Alphaww, BetaStaticTot, BetaPockelsTot, BetaEFISHTot, BetaHRSCase, EletricDipoleTot, Gamma0000, Gammaww00, Gamma2www0, read_file_append, collect_09_A02

log_file_path="/home/florincy/NLO/Dados/pna_gaussian/g09-A02/pNA_g09-A02_gama.log"
version="g09-A02"
with open(log_file_path, "r") as log_file:
    if version=="g09-A02":
        line_1 = collect_limits(log_file)[0]
        line_2=line_1+16
        lines=read_file_append(log_file_path,line_1,line_2)
        print(lines)
        values=collect_09_A02(lines)
        print(values)
            
        
