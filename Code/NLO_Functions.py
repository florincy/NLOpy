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
    gamma_lines=[]
    trash = {"(au)","_|_","Unable", "(z)", "x,y,z", "*", "job", "cpu", "Elapsed", "time", "Dipole polarizability", "First dipole hyperpolarizability", "Second dipole hyperpolarizability", "||"}
    #trash_gamma_efish={"yxxx","zxxx","zyxx","yyyx","xzxx","yzxx","zzyx","zzzx","xxxy","zxxy","yyxy","zyxy","xyyy",""}
    Properties = ["Alpha(-w;w)", "Alpha(0;0):", "Beta(0;0,0):", "Beta(-w;w,0)", "Beta(-2w;w,w)","Gamma(-w;w,0,0)", "Gamma(0;0,0,0):","Gamma(-2w;w,w,0)","Electric dipole moment"]
    Alpha_ok = {"xx", "yy", "zz", "Alpha(-w;w)", "Alpha(0;0):"}
    Beta_ok = {"x", "y", "z", "Beta(0;0,0):", "Beta(-w;w,0)", "Beta(-2w;w,w)","Electric dipole moment"}
    Gamma_EFISH={"xxyy", "xxzz", "yyzz", "xxxx","yyyy","zzzz","xyxy", "xzxz", "yzyz","yxyx","zxzx","zyzy","xyyx","xzzx","yxxy","yzzy","zxxz","zyyz","Gamma(-2w;w,w,0)"}
    Gamma_ok = {"xxyy", "xxzz", "yyzz", "xxxx","yyyy","zzzz","xyxy", "xzxz", "yzyz", "Gamma(0;0,0,0):"}
    Gamma_kerr ={"xxyy", "xxzz", "yyzz", "xxxx","yyyy","zzzz","yyxx", "zzxx", "zzyy","Gamma(-w;w,0,0)"}
    # Thus, xxzz=xzxz, yyzz=yzyz and xxyy=xyxy
    file_lines = file.readlines()
    in_block=False
    lines = []  # Initialize the lines list
    a = "nan"

    for line in file_lines:
        if "Gamma(-2w;w,w,0)" in line:
            a = "Gamma(-2w;w,w,0)"
        if a == "Gamma(-2w;w,w,0)":
            if any(keyword in line for keyword in trash):
                continue
            if any(keyword in line.strip() for keyword in Gamma_EFISH):  
                lines.append(line.strip())  
                # print(line)  # Uncomment for debugging
            if any(keyword in line for keyword in Properties) and "Gamma(-2w;w,w,0)" not in line:
                # print("epa")  # Uncomment for debugging
                a = "nan"  

    a = "nan"
    for line in file_lines:
        if "Gamma(-w;w,0,0)" in line:
            a = "Gamma(-w;w,0,0)"
        if a == "Gamma(-w;w,0,0)":
            if any(keyword in line for keyword in trash):
                continue
            if any(keyword in line.strip() for keyword in Gamma_kerr):  
                lines.append(line.strip())  
                # print(line)  # Uncomment for debugging
            if any(keyword in line for keyword in Properties) and "Gamma(-w;w,0,0)" not in line:
                # print("epa")  # Uncomment for debugging
                a = "nan"   
    for line in file_lines:
        if "Gamma(0;0,0,0):" in line:
            a = "Gamma(0;0,0,0):"
        if a == "Gamma(0;0,0,0):":
            if any(keyword in line for keyword in trash):
                continue
            if any(keyword in line.strip() for keyword in Gamma_ok):  
                lines.append(line.strip())  
                # print(line)  # Uncomment for debugging
            if any(keyword in line for keyword in Properties) and "Gamma(0;0,0,0):" not in line:
                # print("epa")  # Uncomment for debugging
                a = "nan"   
    for line in file_lines:
        if "Beta(0;0,0)" in line:
            a = "Beta(0;0,0)"
        elif "Beta(-w;w,0)" in line:
            a = "Beta(-w;w,0)"
        elif "Beta(-2w;w,w)" in line:
            a = "Beta(-2w;w,w)"
        elif "Electric dipole moment" in line:
            a = "Electric dipole moment"
        if any(keyword in line for keyword in trash):
            continue
        if a in {"Beta(0;0,0)", "Beta(-w;w,0)", "Beta(-2w;w,w)","Electric dipole moment"}:
            if any(keyword in line.split() for keyword in Beta_ok):  
                lines.append(line.strip())  
            if "Electric dipole moment" in line:
                lines.append(line.strip()) 
            if any(keyword in line for keyword in Properties) and a not in line:
                # print("epa")  # Uncomment for debugging
                a = "nan"   
    for line in file_lines:
            if "Alpha(-w;w)" in line:
                a = "Alpha(-w;w)"
            elif "Alpha(0;0):" in line:
                a = "Alpha(0;0):"
            if any(keyword in line for keyword in trash):
                continue
            if a in {"Alpha(-w;w)", "Alpha(0;0):"}:
                if any(keyword in line.split() for keyword in Alpha_ok):  
                    lines.append(line.strip())  
                if any(keyword in line for keyword in Properties) and a not in line:
                    # print("epa")  # Uncomment for debugging
                    a = "nan"   
        
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
    result=math.sqrt(((float(x)/3)**2)+((float(y)/3)**2)+((float(z)/3)**2))
    return result
def betamathb(x,y,z):
    result=math.sqrt(((float(x)/6)**2)+((float(y)/6)**2)+((float(z)/6)**2))
    return result

def BetaStaticTot(list,name,convention="T"):
    Staticlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(0;0,0)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                if convention=="T":
                    au=betamatht(x[1],y[1],z[1])
                    esu=betamatht(x[2],y[2],z[2])
                    SI=betamatht(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=betamathb(x[1],y[1],z[1])
                    esu=betamathb(x[2],y[2],z[2])
                    SI=betamathb(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                Staticlist.append(list[i])
                Staticlist.append(lined_au)
                Staticlist.append(lined_esu)
                Staticlist.append(lined_SI)
    return Staticlist

def BetaHRSTot(list,name,convention="T"):
    HRSlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-2w;w,w)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                if convention=="T":
                    au=betamatht(x[1],y[1],z[1])
                    esu=betamatht(x[2],y[2],z[2])
                    SI=betamatht(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=betamathb(x[1],y[1],z[1])
                    esu=betamathb(x[2],y[2],z[2])
                    SI=betamathb(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                HRSlist.append(list[i])
                HRSlist.append(lined_au)
                HRSlist.append(lined_esu)
                HRSlist.append(lined_SI)
    return HRSlist

def BetaEFISHTot(list,name,convention="T"):
    EFISHlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-w;w,0)' in elem:
                indice=[i,j]
                x=(list[i+1])
                y=(list[i+2])
                z=(list[i+3])
                if convention=="T":
                    au=betamatht(x[1],y[1],z[1])
                    esu=betamatht(x[2],y[2],z[2])
                    SI=betamatht(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=betamathb(x[1],y[1],z[1])
                    esu=betamathb(x[2],y[2],z[2])
                    SI=betamathb(x[3],y[3],z[3])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                EFISHlist.append(list[i])
                EFISHlist.append(lined_au)
                EFISHlist.append(lined_esu)
                EFISHlist.append(lined_SI)
    return EFISHlist
# 3/2 * y(B) = 1/4 * y(T)
# y(B)= 1/36 y(T)
#For now, I figure it out this relations is valid for (-w;w,0,0),(-2w;w,w,0),(0;0,0,0)
def gammamatht(xxxx,yyyy,zzzz,xxyy,xxzz,yyzz):
    result=((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6)+(2*((float(xxyy))/6))+(2*((float(xxzz))/6))+(2*((float(yyzz))/6))/5
    return result
def gammamathb(xxxx,yyyy,zzzz,xxyy,xxzz,yyzz):
    result=((float(xxxx))/36)+((float(yyyy))/36)+((float(zzzz))/36)+(2*((float(xxyy))/36))+(2*((float(xxzz))/36))+(2*((float(yyzz))/36))/5
    return result
def gammamathEFISHt (xxxx,yyyy,zzzz,xyxy,xzxz,yzyz,yxyx,zxzx,zyzy,xyyx,xzzx,yxxy,yzzy,zxxz,zyyz):
    result=(3*((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6))+(2*(((float(xyxy))/6)+((float(xzxz))/6)+((float(yzyz))/6)+((float(yxyx))/6)+((float(zxzx))/6)+((float(zyzy))/6)))+(((float(xyyx))/6)+((float(xzzx))/6)+((float(yxxy))/6)+((float(yzzy))/6)+((float(zxxz))/6)+((float(zyyz))/6))
    return result
def gammamathEFISHb (xxxx,yyyy,zzzz,xyxy,xzxz,yzyz,yxyx,zxzx,zyzy,xyyx,xzzx,yxxy,yzzy,zxxz,zyyz):
    result=(3*((float(xxxx))/36)+((float(yyyy))/36)+((float(zzzz))/36))+(2*(((float(xyxy))/36)+((float(xzxz))/36)+((float(yzyz))/36)+((float(yxyx))/36)+((float(zxzx))/36)+((float(zyzy))/36)))+(((float(xyyx))/36)+((float(xzzx))/36)+((float(yxxy))/36)+((float(yzzy))/36)+((float(zxxz))/36)+((float(zyyz))/36))
    return result
def Gamma0000(list,name,convention):
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
                if convention=="T":
                    au=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    esu=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    SI=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    esu=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    SI=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                gamma0000.append(list[i])
                gamma0000.append(lined_au)
                gamma0000.append(lined_esu)
                gamma0000.append(lined_SI)
    return gamma0000

def Gammaww00(list,name,convention):
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
                if convention=="T":
                    au=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    esu=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    SI=gammamatht(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    esu=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    SI=gammamathb(xxxx[1],yyyy[1],zzzz[1],xxyy[1],xxzz[1],yyzz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                gammaww00.append(list[i])
                gammaww00.append(lined_au)
                gammaww00.append(lined_esu)
                gammaww00.append(lined_SI)
    return gammaww00

def Gamma2www0(list,name,convention):
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
                if convention=="T":
                    au=gammamathEFISHt(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    esu=gammamathEFISHt(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    SI=gammamathEFISHt(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                elif convention=="B":
                    au=gammamathEFISHb(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    esu=gammamathEFISHb(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    SI=gammamathEFISHb(xxxx[1],yyyy[1],zzzz[1],xyxy[1],xzxz[1],yzyz[1])
                    lined_au, lined_esu, lined_SI = Lined(convention, au, esu, SI)
                gamma2www0.append(list[i])
                gamma2www0.append(lined_au)
                gamma2www0.append(lined_esu)
                gamma2www0.append(lined_SI)
                print(gamma2www0)
    return gamma2www0

def Lined(convention, au, esu, SI):
    lined_au=[f"Tot({convention})(au)",au]
    lined_esu=[f"Tot({convention})(esu)",esu]
    lined_SI=[f"Tot({convention})(SI)",SI]
    return lined_au,lined_esu,lined_SI