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

def collect(file):
    lines = []
    trash = ["Unable","xy", "xz", "yx", "yz", "zy", "zx", "(z)","x,y,z","xxx","zzz","yyy","*","job","Alpha (input orientation)","cpu","Elapsed","time","Dipole polarizability","First dipole hyperpolarizability"]
    for line in file:
        if any(element in line for element in trash):
            pass
        elif len(line) > 62:
            pass
        elif "Beta(0;0,0)" in line:
            line="Beta(0;0,0)"
            #print(line)
            lines.append(line.strip())
        elif "Beta(-w;w,0)" in line:
            line="Beta(-w;w,0)"
            #print(line)
            lines.append(line.strip())
        elif "Beta(-2w;w,w)" in line:
            line="Beta(-2w;w,w)"
            #print(line)
            lines.append(line.strip())
        elif "Alpha(-w;w)" in line:
            line="Alpha(-w;w)"
            lines.append(line.strip())
        elif "Alpha(0;0)" in line:
            line="Alpha(0;0)"
            lines.append(line.strip())
        elif "Electric dipole moment" in line:
            line="EletricDipole"
            lines.append(line.strip())
        elif any(keyword in line for keyword in [ "x", "y", "z","xx","yy","zz"]):
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
            lined = [line, name, comment, " "]
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
                #print(x)
                a_au=((float(x[1]))+(float(y[1]))+(float(z[1])))/3
                a_debye=((float(x[1]))+(float(y[1]))+(float(z[1])))/3
                a_SI=((float(x[1]))+(float(y[1]))+(float(z[1])))/3
                #print(x)
                lined_au=["Tot(Alpha)(au)",a_au,"",""]
                lined_debye=["Tot(Alpha)(Debye)",a_debye,"",""]
                lined_SI=["Tot(Alpha)(SI)",a_SI,"",""]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist

def EletricDipoleTot(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'EletricDipole' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                d_au=math.sqrt(((float(x[1]))**2)+((float(y[1]))**2)+((float(z[1]))**2))
                d_debye=math.sqrt(((float(x[2]))**2)+((float(y[2]))**2)+((float(z[2]))**2))
                d_SI=math.sqrt(((float(x[3]))**2)+((float(y[3]))**2)+((float(z[3]))**2))
                #print(x)
                lined_au=["Tot(Electric Dipole)(au)",d_au,"",""]
                lined_debye=["Tot(Electric Dipole)(Debye)",d_debye,"",""]
                lined_SI=["Tot(Electric Dipole)(SI)",d_SI,"",""]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist

def BetaStaticTot(list,name):
    Staticlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=math.sqrt(((float(x[1])/3)**2)+((float(y[1])/3)**2)+((float(z[1])/3)**2))
                b_au=math.sqrt(((float(x[1])/6)**2)+((float(y[1])/6)**2)+((float(z[1])/6)**2))
                t_esu=math.sqrt(((float(x[2])/3)**2)+((float(y[2])/3)**2)+((float(z[2])/3)**2))
                b_esu=math.sqrt(((float(x[2])/6)**2)+((float(y[2])/6)**2)+((float(z[2])/6)**2))
                t_SI=math.sqrt(((float(x[3])/3)**2)+((float(y[3])/3)**2)+((float(z[3])/3)**2))
                b_SI=math.sqrt(((float(x[3])/6)**2)+((float(y[3])/6)**2)+((float(z[3])/6)**2))
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if 'Beta(0;0,0)' in elem:
                    Staticlist.append(list[i])
                    Staticlist.append(lined_au)
                    Staticlist.append(lined_esu)
                    Staticlist.append(lined_SI)
    return Staticlist
def BetaHRSTot(list,name):
    HRSlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=math.sqrt(((float(x[1])/3)**2)+((float(y[1])/3)**2)+((float(z[1])/3)**2))
                b_au=math.sqrt(((float(x[1])/6)**2)+((float(y[1])/6)**2)+((float(z[1])/6)**2))
                t_esu=math.sqrt(((float(x[2])/3)**2)+((float(y[2])/3)**2)+((float(z[2])/3)**2))
                b_esu=math.sqrt(((float(x[2])/6)**2)+((float(y[2])/6)**2)+((float(z[2])/6)**2))
                t_SI=math.sqrt(((float(x[3])/3)**2)+((float(y[3])/3)**2)+((float(z[3])/3)**2))
                b_SI=math.sqrt(((float(x[3])/6)**2)+((float(y[3])/6)**2)+((float(z[3])/6)**2))
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if 'Beta(-2w;w,w)' in elem:
                    HRSlist.append(list[i])
                    HRSlist.append(lined_au)
                    HRSlist.append(lined_esu)
                    HRSlist.append(lined_SI)
    return HRSlist

def BetaEFISHTot(list,name):
    EFISHlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-w;w,0)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=math.sqrt(((float(x[1])/3)**2)+((float(y[1])/3)**2)+((float(z[1])/3)**2))
                b_au=math.sqrt(((float(x[1])/6)**2)+((float(y[1])/6)**2)+((float(z[1])/6)**2))
                t_esu=math.sqrt(((float(x[2])/3)**2)+((float(y[2])/3)**2)+((float(z[2])/3)**2))
                b_esu=math.sqrt(((float(x[2])/6)**2)+((float(y[2])/6)**2)+((float(z[2])/6)**2))
                t_SI=math.sqrt(((float(x[3])/3)**2)+((float(y[3])/3)**2)+((float(z[3])/3)**2))
                b_SI=math.sqrt(((float(x[3])/6)**2)+((float(y[3])/6)**2)+((float(z[3])/6)**2))
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if "Beta(-w;w,0)" in elem:
                    EFISHlist.append(list[i])
                    EFISHlist.append(lined_au)
                    EFISHlist.append(lined_esu)
                    EFISHlist.append(lined_SI)
    return EFISHlist



