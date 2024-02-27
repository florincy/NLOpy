import tkinter as tk
from tkinter import filedialog
import os
import csv
import math
def collect_limits(log_file):
    line1, line2 = None, None
    for num, line in enumerate(log_file, 1):
        if "Electric dipole moment (input orientation):" in line:
            line1 = num
        if "Electric dipole moment (dipole orientation):" in line:
            line2 = num
    return line1, line2

def collect(file):
    lines = []
    trash = ["Unable","xy", "xz", "xx", "yx", "yz", "yy", "zy", "zx", "zz", "(z)","x,y,z","*","job","Alpha (input orientation)","cpu","Elapsed","time","Dipole polarizability"]
    for line in file:
        if any(element in line for element in trash):
            pass
        elif len(line) > 61:
            pass
        elif "Beta(-w;w,0)" in line:
            line="Beta(-w;w,0)"
            lines.append(line.strip())
        elif "Beta(-2w;w,0)" in line:
            line="Beta(-2w;w,w)"
            lines.append(line.strip())
        elif "First dipole hyperpolarizability" in line:
            line="Alpha"
            lines.append(line.strip())
        elif "Electric dipole moment" in line:
            line="EletricDipole"
            lines.append(line.strip())
        elif any(keyword in line for keyword in [ "x", "y", "z"]):
            lines.append(line.strip())      

    return lines

def calc(file, name, comment):
    lines = []
    for line in file:
        if any(keyword in line for keyword in ["x", "y", "z"]):
            line = line.split()
            for i in range(len(line)):
                line[i] = line[i].replace('D', 'E')
            lines.append(line)
        else:
            lined = [line, name, comment, "null"]
            lines.append(lined)
    return lines

def GammaTot(list, name):
    print("We are still working on this property")

def AlphaTot(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Alpha' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                a_au=math.sqrt(((float(x[1]))**2)+((float(y[1]))**2)+((float(z[1]))**2))
                a_debye=math.sqrt(((float(x[2]))**2)+((float(y[2]))**2)+((float(z[2]))**2))
                a_SI=math.sqrt(((float(x[3]))**2)+((float(y[3]))**2)+((float(z[3]))**2))
                lined_au=["Tot(Alpha)(au)",a_au,"null","null"]
                lined_debye=["Tot(Alpha)(Debye)",a_debye,"null","null"]
                lined_SI=["Tot(Alpha)(SI)",a_SI,"null","null"]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist

def EletricDipoleTot(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                d_au=math.sqrt(((float(x[1]))**2)+((float(y[1]))**2)+((float(z[1]))**2))
                d_debye=math.sqrt(((float(x[2]))**2)+((float(y[2]))**2)+((float(z[2]))**2))
                d_SI=math.sqrt(((float(x[3]))**2)+((float(y[3]))**2)+((float(z[3]))**2))
                print(x)
                lined_au=["Tot(Electric Dipole)(au)",d_au,"null","null"]
                lined_debye=["Tot(Electric Dipole)(Debye)",d_debye,"null","null"]
                lined_SI=["Tot(Electric Dipole)(SI)",d_SI,"null","null"]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist

def BetaTot(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=math.sqrt(((float(x[1])/3)**2)+((float(y[1])/3)**2)+((float(z[1])/3)**2))
                p_au=math.sqrt(((float(x[1])/6)**2)+((float(y[1])/6)**2)+((float(z[1])/6)**2))
                t_esu=math.sqrt(((float(x[2])/3)**2)+((float(y[2])/3)**2)+((float(z[2])/3)**2))
                p_esu=math.sqrt(((float(x[2])/6)**2)+((float(y[2])/6)**2)+((float(z[2])/6)**2))
                t_SI=math.sqrt(((float(x[3])/3)**2)+((float(y[3])/3)**2)+((float(z[3])/3)**2))
                p_SI=math.sqrt(((float(x[3])/6)**2)+((float(y[3])/6)**2)+((float(z[3])/6)**2))
                print(x)
                lined_au=["Tot(t)(au)",t_au,"Top(p)(au)",p_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(p)(esu)",p_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(p)(SI)",p_SI]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_esu)
                nwlist.append(lined_SI)
    return nwlist
        
def read_file(log_file_path, start, end=None):
    lines = []
    if end is None:
        with open(log_file_path, "r") as log_file:
            for i in range(start - 2):
                next(log_file)  # Skip lines until start line
            for line in log_file:
                lines.append(line.strip())
    else:
        with open(log_file_path, "r") as log_file:
            for i in range(start - 2):
                next(log_file)  # Skip lines until start line
            
            for i in range(end - start + 1):
                lines.append(next(log_file).strip())
    return lines
root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()

# iterating over all files

for path, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith(".log"):
            print(name) 
            log_file_path = os.path.join(path, name)
            print(f"Processing file: {log_file_path}")
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
                    comment="Input Orientation"
                    ret = calc(file,name,comment)
                    beta=BetaTot(ret,name)
                    dipole=EletricDipoleTot(ret,name)
                    alpha=AlphaTot(ret,name)
                    writer.writerows(beta)
                    writer.writerows(dipole)
                    print(alpha)
                    writer.writerows(alpha)
                with open(outputDipolePath, "r") as file:
                    comment="Dipole Orientation"
                    ret = calc(file,name,comment)
                    beta=BetaTot(ret,name)
                    dipole=EletricDipoleTot(ret,name)
                    alpha=AlphaTot(ret,name)
                    writer.writerows(beta)
                    writer.writerows(dipole)
                    writer.writerows(alpha)

