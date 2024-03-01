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

def read_file(log_file_path, start, end=None):
    lines = []
    with open(log_file_path, "r") as log_file:
        for i in range(start - 2):
            next(log_file)  # Skip lines until start line
            
        if end is None:
            for line in log_file:
                lines.append(line.strip())
        else:
            for i in range(end - start + 1):
                lines.append(next(log_file).strip())
    return lines

def open_file(log_file_path):
    with open(log_file_path, "r") as log_file:
        return log_file.readlines()

def collect(file):
    lines = []
    trash = {"Unable", "(z)", "x,y,z", "*", "job", "(input orientation)", "cpu", "Elapsed", "time", "Dipole polarizability", "First dipole hyperpolarizability", "Second dipole hyperpolarizability", "||"}
    Properties = ["Alpha", "Beta", "Gamma"]
    Alpha_ok = {"xx", "yy", "zz", "Alpha(-w;w)", "Alpha(0;0):"}
    Beta_ok = {"x", "y", "z", "Beta(0;0,0):", "Beta(-w;w,0)", "Beta(-2w;w,w)"}
    Gamma_ok = {"xxyy", "xxzz", "yyzz", "xxxx","yyyy","zzzz","xyxy", "xzxz", "yzyz","Gamma(-w;w,0,0)", "Gamma(0;0,0,0):","Gamma(-2w;w,w,0)"}
    # Thus, xxzz=xzxz, yyzz=yzyz and xxyy=xyxy
    file_lines = file.readlines()

    for line in file_lines:
        if any(keyword in line for keyword in trash):
            continue

        # Check for Alpha property
        if any(keyword in line.split() for keyword in Alpha_ok):
            lines.append(line.strip())
            continue

    for line in file_lines:
        if "Electric dipole moment" in line:
            lines.append(line.strip())
            continue

    for line in file_lines:
        if any(keyword in line for keyword in trash):
            continue

        # Check for Beta property
        if any(keyword in line.split() for keyword in Beta_ok):
            lines.append(line.strip())
            continue

    for line in file_lines:
        if any(keyword in line for keyword in trash):
            continue

        # Check for Gamma property
        if any(keyword in line.split() for keyword in Gamma_ok):
            lines.append(line.strip())
    '''
    for line in file_lines:
        if any(keyword in line for keyword in trash):
            continue

        # Check for Gamma property
        if any(keyword in line.split() for keyword in Gamma2www0_ok):
            lines.append(line.strip())
'''
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

def AlphaStatic(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Alpha(0;0)' in elem:
                indice=[i,j]
                xx=(list[i+1])
                yy=(list[i+2])
                zz=(list[i+3])
                def alphamath(xx,yy,zz):
                    result=((float(xx))+(float(yy))+(float(zz)))/3
                    return result
                a_au=alphamath(xx[1],yy[1],zz[1])
                a_debye=alphamath(xx[2],yy[2],zz[2])
                a_SI=alphamath(xx[3],yy[3],zz[3])
                lined_au=["Tot(Alpha)(au)",a_au,"",""]
                lined_debye=["Tot(Alpha)(Debye)",a_debye,"",""]
                lined_SI=["Tot(Alpha)(SI)",a_SI,"",""]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist

def Alphaww(list,name):
    nwlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Alpha(-w;w)' in elem:
                indice=[i,j]
                xx=(list[i+1])
                yy=(list[i+2])
                zz=(list[i+3])
                def alphamath(xx,yy,zz):
                    result=((float(xx))+(float(yy))+(float(zz)))/3
                    return result
                a_au=alphamath(xx[1],yy[1],zz[1])
                a_debye=alphamath(xx[2],yy[2],zz[2])
                a_SI=alphamath(xx[3],yy[3],zz[3])
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
                def electricdipolemath(x,y,z):
                    result=math.sqrt((float(x)**2)+((float(y))**2)+((float(z))**2))
                    return result
                d_au=electricdipolemath(x[1],y[1],z[1])
                d_debye=electricdipolemath(x[2],y[2],z[2])
                d_SI=electricdipolemath(x[3],y[3],z[3])
                lined_au=["Tot(Electric Dipole)(au)",d_au,"",""]
                lined_debye=["Tot(Electric Dipole)(Debye)",d_debye,"",""]
                lined_SI=["Tot(Electric Dipole)(SI)",d_SI,"",""]
                nwlist.append(list[i])
                nwlist.append(lined_au)
                nwlist.append(lined_debye)
                nwlist.append(lined_SI)
    return nwlist
def betamatht(x,y,z):
    result=math.sqrt(((float(x)/2)**2)+((float(y)/2)**2)+((float(z)/2)**2))
    return result
def betamathb(x,y,z):
    result=math.sqrt(((float(x)/4)**2)+((float(y)/4)**2)+((float(z)/4)**2))
    return result
def BetaStaticTot(list,name):
    Staticlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(0;0,0)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=betamatht(x[1],y[1],z[1])
                b_au=betamathb(x[1],y[1],z[1])
                t_esu=betamatht(x[2],y[2],z[2])
                b_esu=betamathb(x[2],y[2],z[2])
                t_SI=betamatht(x[3],y[3],z[3])
                b_SI=betamathb(x[3],y[3],z[3])
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
            if 'Beta(-2w;w,w)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                t_au=betamatht(x[1],y[1],z[1])
                b_au=betamathb(x[1],y[1],z[1])
                t_esu=betamatht(x[2],y[2],z[2])
                b_esu=betamathb(x[2],y[2],z[2])
                t_SI=betamatht(x[3],y[3],z[3])
                b_SI=betamathb(x[3],y[3],z[3])
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
                t_au=betamatht(x[1],y[1],z[1])
                b_au=betamathb(x[1],y[1],z[1])
                t_esu=betamatht(x[2],y[2],z[2])
                b_esu=betamathb(x[2],y[2],z[2])
                t_SI=betamatht(x[3],y[3],z[3])
                b_SI=betamathb(x[3],y[3],z[3])
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if "Beta(-w;w,0)" in elem:
                    EFISHlist.append(list[i])
                    EFISHlist.append(lined_au)
                    EFISHlist.append(lined_esu)
                    EFISHlist.append(lined_SI)
    return EFISHlist
def gammamatht(xxxx,yyyy,zzzz,xxyy,xxzz,yyzz):
    result=((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6)+(2*((float(xxyy))/6))+(2*((float(xxzz))/6))+(2*((float(yyzz))/6))/5
    return result
def gammamathb(xxxx,yyyy,zzzz,xxyy,xxzz,yyzz):
    result=((float(xxxx))/36)+((float(yyyy))/36)+((float(zzzz))/36)+(2*((float(xxyy))/36))+(2*((float(xxzz))/36))+(2*((float(yyzz))/36))/5
    return result
def Gamma0000(list,name):
    gamma0000=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(0;0,0,0)' in elem:
                indice=[i,j]
                xxxx=(list[i+1])
                xxyy=(list[i+2])
                yyyy=(list[i+2])
                xxzz=(list[i+2])
                yyzz=(list[i+2])
                zzzz=(list[i+3])
                t_au=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                t_esu=gammamatht(xxxx[2],yyyy[2],zzzz[2],xxyy[2],xxzz[2],yyzz[2])
                t_SI=gammamatht(xxxx[3],yyyy[3],zzzz[3],xxyy[3],xxzz[3],yyzz[3])
                b_au=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                b_esu=gammamathb(xxxx[2],yyyy[2],zzzz[2],xxyy[2],xxzz[2],yyzz[2])
                b_SI=gammamathb(xxxx[3],yyyy[3],zzzz[3],xxyy[3],xxzz[3],yyzz[3])
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if "Gamma(0;0,0,0)" in elem:
                    gamma0000.append(list[i])
                    gamma0000.append(lined_au)
                    gamma0000.append(lined_esu)
                    gamma0000.append(lined_SI)
    return gamma0000

def Gammaww00(list,name):
    gammaww00=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(-w;w,0,0)' in elem:
                indice=[i,j]
                xxxx=(list[i+1])
                xxyy=(list[i+2])
                yyyy=(list[i+2])
                xxzz=(list[i+2])
                yyzz=(list[i+2])
                zzzz=(list[i+3])
                t_au=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                t_esu=gammamatht(xxxx[2],yyyy[2],zzzz[2],xxyy[2],xxzz[2],yyzz[2])
                t_SI=gammamatht(xxxx[3],yyyy[3],zzzz[3],xxyy[3],xxzz[3],yyzz[3])
                b_au=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                b_esu=gammamathb(xxxx[2],yyyy[2],zzzz[2],xxyy[2],xxzz[2],yyzz[2])
                b_SI=gammamathb(xxxx[3],yyyy[3],zzzz[3],xxyy[3],xxzz[3],yyzz[3])
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if "Gamma(-w;w,0,0)" in elem:
                    gammaww00.append(list[i])
                    gammaww00.append(lined_au)
                    gammaww00.append(lined_esu)
                    gammaww00.append(lined_SI)
    return gammaww00

def Gamma2www0(list,name):
    gamma2www0=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(-2w;w,w,0)' in elem:
                indice=[i,j]
                xxxx=(list[i+1])
                xyxy=(list[i+2])
                yyyy=(list[i+2])
                xzxz=(list[i+2])
                yzyz=(list[i+2])
                zzzz=(list[i+3])
                #ijkl = ikjl
                # Thus, xxzz=xzxz, yyzz=yzyz and xxyy=xyxy                
                t_au=gammamatht(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                t_esu=gammamatht(xxxx[2],yyyy[2],zzzz[2],xyxy[2],xzxz[2],yzyz[2])
                t_SI=gammamatht(xxxx[3],yyyy[3],zzzz[3],xyxy[3],xzxz[3],yzyz[3])
                b_au=gammamathb(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                b_esu=gammamathb(xxxx[2],yyyy[2],zzzz[2],xyxy[2],xzxz[2],yzyz[2])
                b_SI=gammamathb(xxxx[3],yyyy[3],zzzz[3],xyxy[3],xzxz[3],yzyz[3])
                lined_au=["Tot(t)(au)",t_au,"Top(b)(au)",b_au]
                lined_esu=["Tot(t)(esu)",t_esu,"Top(b)(esu)",b_esu]
                lined_SI=["Tot(t)(SI)",t_SI,"Top(b)(SI)",b_SI]
                if "Gamma(-2w;w,w,0)" in elem:
                    gamma2www0.append(list[i])
                    gamma2www0.append(lined_au)
                    gamma2www0.append(lined_esu)
                    gamma2www0.append(lined_SI)
    return gamma2www0

