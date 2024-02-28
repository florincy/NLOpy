import tkinter as tk
from tkinter import filedialog
import os
import csv
import math
from NLO_Functions import collect_limits, collect, read_file, calc, AlphaTot, BetaStaticTot, BetaHRSTot, BetaEFISHTot, EletricDipoleTot, Gamma0000, Gammaww00

root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()

# iterating over all files

for path, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith(".log"):
            log_file_path = os.path.join(path, name)
            returns = collect_limits(open(log_file_path, "r"))
            line1 = returns[0]
            line2 = returns[1]
            input_ref = read_file(log_file_path, line1, line2)
            input_dip=read_file(log_file_path,line2)
            # Write the lines obtained from the file to a new file
            output_file_path_dipole=os.path.join(path,"DipoleRerence.txt")
            output_file_path_input=os.path.join(path,"InputReference.txt")
            with open(output_file_path_dipole, "w") as output_file:
                for line in input_dip:
                    output_file.write(line + "\n")
            with open(output_file_path_input, "w") as output_file:
                for line in input_ref:
                    output_file.write(line + "\n")

#Lets write all of this in a result file for Input
            outputInputPath=os.path.join(directory,"ResultInp.txt")     
            outputDipolePath=os.path.join(directory,"ResultDip.txt")   

            with open(outputInputPath, "w") as outputInput:
                with open(output_file_path_input, "r") as file:
                    lines=collect(file)
                    for line in lines:
                        outputInput.write(line+"\n")

            with open(outputDipolePath, "w") as outputDipole:
                with open(output_file_path_dipole, "r") as file:
                    lines=collect(file)
                    for line in lines:
                        outputDipole.write(line+"\n")    
            with open('output.csv', 'a', newline='') as df:
                writer = csv.writer(df)
                with open(outputInputPath, "r") as file:
                    comment="Dipole Orientation"
                    ret = calc(file,name,comment)
                    gamma0000=Gamma0000(ret,name)
                    #print(gamma0000)
                    gammaww00=Gammaww00(ret,name)
                    print(gammaww00)
                    '''
                    beta=BetaStaticTot(ret,name)
                    #print(beta)
                    beta=BetaEFISHTot(ret,name)
                    #print(beta)
                    beta=BetaHRSTot(ret,name)
                    #print(beta)
                    dipole=EletricDipoleTot(ret,name)
                    alpha=AlphaTot(ret,name)
                    writer.writerows(beta)
                    writer.writerows(dipole)
                    writer.writerows(alpha)
                    '''
                with open(outputDipolePath, "r") as file:
                    comment="Dipole Orientation"
                    ret = calc(file,name,comment)
                    '''
                    beta=BetaStaticTot(ret,name)
                    print(beta)
                    beta=BetaEFISHTot(ret,name)
                    print(beta)
                    beta=BetaHRSTot(ret,name)
                    print(beta)
                    dipole=EletricDipoleTot(ret,name)
                    alpha=AlphaTot(ret,name)
                    writer.writerows(beta)
                    writer.writerows(dipole)
                    writer.writerows(alpha)
                    '''

