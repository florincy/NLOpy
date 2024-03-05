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
    beta_lines=[]
    trash = {"(au)","_|_","Unable", "(z)", "x,y,z", "*", "job", "cpu", "Elapsed", "time", "Dipole polarizability", "First dipole hyperpolarizability", "Second dipole hyperpolarizability", "||"}
    #trash_gamma_efish={"yxxx","zxxx","zyxx","yyyx","xzxx","yzxx","zzyx","zzzx","xxxy","zxxy","yyxy","zyxy","xyyy",""}
    Properties = ["Alpha(-w;w)", "Alpha(0;0):", "Beta(0;0,0):", "Beta(-w;w,0)", "Beta(-2w;w,w)","Gamma(-w;w,0,0)", "Gamma(0;0,0,0):","Gamma(-2w;w,w,0)","Electric dipole moment"]
    Alpha_ok = {"xx", "yy", "zz", "Alpha(-w;w)", "Alpha(0;0):"}
    Beta_HRS={"Beta(-2w;w,w)","xxx","yyy","zzz","xyx","xzx","yyx","yzy","zzx","zzy","xyy","xzz","yxx","yzz","zxx","zyy","xyz","xzy","zxy","zyx","yxz","yzx"}
    Beta_ok = {"x", "y", "z", "Beta(0;0,0):", "Beta(-w;w,0)", "Beta(-2w;w,w)","Electric dipole moment"}
    Gamma_EFISH={"xxyy", "xxzz", "yyzz", "xxxx","yyyy","zzzz","xyxy", "xzxz", "yzyz","yyxx","zzxx","zzyy","xyyx","xzzx","yxxy","yzzy","zxxz","zyyz","Gamma(-2w;w,w,0)"}
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
    for line in file_lines:
        if "Beta(-2w;w,w)" in line:
            a = "Beta(-2w;w,w)"
        if a == "Beta(-2w;w,w)":
            if any(keyword in line for keyword in trash):
                continue
            if any(keyword in line.strip() for keyword in Beta_HRS):  
                beta_lines.append(line.strip())  
                # print(line)  # Uncomment for debugging
            if any(keyword in line for keyword in Properties) and "Beta(-2w;w,w)" not in line:
                # print("epa")  # Uncomment for debugging
                a = "nan" 

        
        
    return lines,beta_lines


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

def alphamath(xx,yy,zz):
    result=((float(xx))+(float(yy))+(float(zz)))/3
    return result

def namingUnits(unit):
    if unit==1:
        return "au"
    elif unit==2:
        return "esu"
    elif unit==3:
        return "SI"

def AlphaStatic(list, name, unit,components=False):
    AlphaStaticList = []
    for i, sublist in enumerate(list):
        for j, elem in enumerate(sublist):
            if 'Alpha(0;0):' in elem:
                xx = list[i+1]
                yy = list[i+2]
                zz = list[i+3]
                tensors_c=[xx,yy,zz]
                a = alphamath(xx[unit], yy[unit], zz[unit])
                lined = ["Tot(Alpha)({})".format(namingUnits(unit)), a, "", ""]
                AlphaStaticList.append(list[i])
                AlphaStaticList.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        AlphaStaticList.append(lined_component)                
    return AlphaStaticList


def Alphaww(list,name,unit,components=False):
    AlphawwList=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Alpha(-w;w)' in elem:
                xx=list[i+1]
                yy=list[i+2]
                zz=list[i+3]
                tensors_c=[xx,yy,zz]
                a=alphamath(xx[unit],yy[unit],zz[unit])
                lined = ["Tot(Alpha)({})".format(namingUnits(unit)), a, "", ""]
                AlphawwList.append(list[i])
                AlphawwList.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        AlphawwList.append(lined_component)
    return AlphawwList

def EletricDipoleTot(list,name,unit,components=False):
    ElectricDipoleList=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Electric dipole ' in elem:
                x=list[i+1]
                y=list[i+2]
                z=list[i+3]
                tensors_c=[x,y,z]
                def electricdipolemath(x,y,z):
                    result=math.sqrt((float(x)**2)+((float(y))**2)+((float(z))**2))
                    return result
                d=electricdipolemath(x[unit],y[unit],z[unit])
                print(d)
                lined=["Tot(Electric Dipole)(Debye)",d,"",""]
                ElectricDipoleList.append(list[i])
                ElectricDipoleList.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} (Debye)".format(component[0]),component[unit],"",""]
                        ElectricDipoleList.append(lined_component)
    return ElectricDipoleList
def betamatht(x,y,z):
    result=math.sqrt(((float(x)/3)**2)+((float(y)/3)**2)+((float(z)/3)**2))
    return result
def betamathb(x,y,z):
    result=math.sqrt(((float(x)/6)**2)+((float(y)/6)**2)+((float(z)/6)**2))
    return result

def BetaStaticTot(list,name,convention="T",unit=None,components=False):
    Staticlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(0;0,0)' in elem:
                x=list[i+1]
                y=list[i+2]
                z=list[i+3]
                tensors_c=[x,y,z]
                if convention=="T":
                    b=betamathb(x[unit],y[unit],z[unit])
                elif convention=="B":
                    b=betamatht(x[unit],y[unit],z[unit])
                lined = ["Tot(Beta)({})({})".format(namingUnits(unit), convention), b, "", ""]
                Staticlist.append(list[i])
                Staticlist.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        Staticlist.append(lined_component)
    return Staticlist

def BetaHRSTot(list,name,convention="T",unit=None,components=False):
    HRSlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-2w;w,w)' in elem:
                x=list[i+1]
                y=list[i+2]
                z=list[i+3]
                tensors_c=[x,y,z]
                if convention=="T":
                    b=betamathb(x[unit],y[unit],z[unit])
                elif convention=="B":
                    b=betamatht(x[unit],y[unit],z[unit])
                lined = ["Tot(Beta)({})({})".format(namingUnits(unit), convention), b, "", ""]
                HRSlist.append(list[i])
                HRSlist.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        HRSlist.append(lined_component)
    return HRSlist

def BetaEFISHTot(list,name,convention="T",unit=None,components=False):
    EFISHlist=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-w;w,0)' in elem:
                x=list[i+1]
                y=list[i+2]
                z=list[i+3]
                tensors_c=[x,y,z]
                if convention=="T":
                    b=betamathb(x[unit],y[unit],z[unit])
                elif convention=="B":
                    b=betamatht(x[unit],y[unit],z[unit])
                lined = ["Tot(Beta)({})({})".format(namingUnits(unit), convention), b, "", ""]
                EFISHlist.append(list[i])
                EFISHlist.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        EFISHlist.append(lined_component)
    return EFISHlist
def betaHRSmath(xxx,yxx,zxx,xyx,yyx,zyx,xyy,yyy,zyy,xzx,yzx,zzx,xzy,yzy,zzy,xzz,yzz,zzz):
    #beta_abc = beta_acb
    #xxy=xyx
    #xxz=xzx
    #xyz=xzy
    #yxz=yzx
    #zxy=zyx
    t1=((((float(xxx))**2)+((float(yyy))**2)+((float(zzz))**2)))
    t2=((((float(xyx))**2)+((float(xzx))**2)+((float(yyx))**2)+((float(yzy))**2)+((float(zzx))**2)+((float(zzy))**2)))
    t3=((((float(xxx))*(float(xyy)))+((float(xxx))*(float(xzz)))+((float(yyy))*(float(yxx)))+((float(yyy))*(float(yzz)))+((float(zzz))*(float(zxx)))+((float(zzz))*(float(zyy)))))
    t4 = (((float(xyy)) * (float(yyx)) + (float(xzz)) * (float(xzx)) + (float(yzz)) * (float(zzy)) + (float(yxx)) * (float(xyy)) + (float(zxx)) * (float(xzz)) + (float(zyy)) * (float(yzz))))
    t5=((((float(xxx))*(float(yyx)))+((float(xxx))*(float(zzx)))+((float(yyy))*(float(xyx)))+((float(yyy))*(float(zzy)))+((float(zzz))*(float(xzx)))+((float(zzz))*(float(yzy)))))
    t6=((((float(yxx))**2)+((float(yzz))**2)+((float(xyy))**2)+((float(xzz))**2)+((float(zyy))**2)+((float(zxx))**2)))
    t7=(((float(yyx)) * (float(xzz)) + (float(zzx)) * (float(xyy)) + (float(xyx)) * (float(yzz)) + (float(zzy)) * (float(yxx)) + (float(xzx)) * (float(zyy)) + (float(yzy)) * (float(zxx))))
    t8=(((float(xyy)) * (float(xzz)) + (float(xzz)) * (float(xyy)) + (float(yxx)) * (float(yzz)) + (float(yzz)) * (float(yxx)) + (float(zxx)) * (float(zyy)) + (float(zyy)) * (float(zxx))))
    t9=(((float(yyx)) * (float(zzx)) + (float(zzx)) * (float(yyx)) + (float(xyx)) * (float(zzy)) + (float(zzy)) * (float(xyx)) + (float(xzx)) * (float(yzy)) + (float(yzy)) * (float(xzx))))
    t10=(((float(xzy))**2)+((float(xzy))**2)+((float(yzx))**2)+((float(yzx))**2)+((float(zyx))**2)+((float(zyx))**2))
    # t11=((float(xyz))*((float(yxz))))+((float(xzy))*((float(zxy))))+((float(yzx))*((float(zxy))))+((float(yxz))*((float(xzy))))+((float(zxy))*(float(xzy)))+((float(zyx))*(float(yzx)))
    t11=((float(xzy))*((float(yzx))))+((float(xzy))*((float(zyx))))+((float(yzx))*((float(zyx))))+((float(yzx))*((float(xzy))))+((float(zyx))*(float(xzy)))+((float(zyx))*(float(yzx)))
    bzzz=(t1*(1/7))+(t2*(4/35))+(t3*(2/35))+(t4*(4/35))+(t5*(4/35))+(t6*(1/35))+(t7*(4/105))+(t8*(1/105))+(t9*(4/105))+(t10*(4/105))+(t11*(4/105))
    bzxx=(t1*(1/35))+(t3*(4/105))+(t5*(-2/35))+(t2*(8/105))+(t6*(3/35))+(t4*(-2/35))+(t8*(1/35))+(t9*(-2/105))+(t7*(-2/105))+(t10*(2/35))+(t11*(-2/105))
def BetaHRSCase(list,name,convention="T",unit=None,components=False):
    HRSlist=[]
    #[['Beta(-2w;w,w) w=  432.0nm:', 'ferro_pbe0_polar.log', 'Dipole Orientation', ' '], ['xxx', '-0.128728E+00', '-0.111211E-02', '-0.412748E-03'], ['yxx', '-0.759067E+00', '-0.655775E-02', '-0.243384E-02'], ['zxx', '-0.428911E+00', '-0.370546E-02', '-0.137524E-02'], ['yyx', '-0.714938E+00', '-0.617650E-02', '-0.229235E-02'], ['zyx', '-0.339588E+00', '-0.293377E-02', '-0.108884E-02'], ['xyy', '-0.143306E+00', '-0.123805E-02', '-0.459491E-03'], ['yyy', '0.766277E+00', '0.662003E-02', '0.245696E-02'], ['zyy', '-0.679120E+00', '-0.586706E-02', '-0.217750E-02'], ['yzx', '-0.179569E+00', '-0.155134E-02', '-0.575765E-03'], ['zzx', '0.193351E+00', '0.167040E-02', '0.619954E-03'], ['xzy', '-0.257625E-01', '-0.222568E-03', '-0.826037E-04'], ['zzy', '0.491069E-01', '0.424246E-03', '0.157455E-03'], ['xzz', '-0.322233E+00', '-0.278384E-02', '-0.103319E-02'], ['yzz', '0.238276E+00', '0.205852E-02', '0.763999E-03'], ['zzz', '0.331969E+00', '0.286795E-02', '0.106441E-02']]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Beta(-2w;w,w)' in elem:
                xxx=list[i+1]
                yxx=list[i+2]
                zxx=list[i+3]
                xyx=list[i+4]
                yyx=list[i+5]
                zyx=list[i+6]
                xyy=list[i+7]
                yyy=list[i+8]
                zyy=list[i+9]
                xzx=list[i+10]
                yzx=list[i+11]
                zzx=list[i+12]
                xzy=list[i+13]
                yzy=list[i+14]
                zzy=list[i+15]
                xzz=list[i+16]
                yzz=list[i+17]
                zzz=list[i+18]

# 3/2 * y(B) = 1/4 * y(T)
# y(B)= 1/36 y(T)
#For now, I figure it out this relations is valid for (-w;w,0,0),(-2w;w,w,0),(0;0,0,0)
def gammamatht(xxxx,yyyy,zzzz,xxyy,xxzz,yyzz):
    result=(((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6)+(2*((float(xxyy))/6))+(2*((float(xxzz))/6))+(2*((float(yyzz))/6)))/5
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
def gammamathKerrt(xxxx,yyyy,zzzz,xxyy,yyxx,xxzz,zzxx,yyzz,zzyy):
    result=(((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6)+(((float(xxyy))/6))+(((float(yyxx))/6))+(((float(xxzz))/6))+(((float(zzxx))/6))+((float(yyzz))/6)+((float(zzyy))/6))/5
    return result
def gammamathKerrb(xxxx,yyyy,zzzz,xxyy,yyxx,xxzz,zzxx,yyzz,zzyy):
    result=(((float(xxxx))/36)+((float(yyyy))/36)+((float(zzzz))/36)+(((float(xxyy))/36))+(((float(yyxx))/36))+(((float(xxzz))/36))+(((float(zzxx))/36))+((float(yyzz))/36)+((float(zzyy))/36))/5
    return result
def Gamma0000(list,name,convention,unit,components=False):
    gamma0000=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(0;0,0,0)' in elem:
                xxxx=list[i+1]
                xxyy=list[i+2]
                yyyy=list[i+3]
                xxzz=list[i+4]
                yyzz=list[i+5]
                zzzz=list[i+6]
                tensors_c=[xxxx,yyyy,zzzz,xxyy,xxzz,yyzz]
                if convention=="T":
                    g=gammamatht(xxxx[unit],yyyy[unit],zzzz[unit],xxyy[unit],xxzz[unit],yyzz[unit])
                elif convention=="B":
                    g=gammamathb(xxxx[unit],yyyy[unit],zzzz[unit],xxyy[unit],xxzz[unit],yyzz[unit])
                lined = ["Tot(Gamma)({})({})".format(namingUnits(unit), convention), g, "", ""]
                gamma0000.append(list[i])
                gamma0000.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        gamma0000.append(lined_component)
    return gamma0000

def Gammaww00(list,name,convention,unit,components=False):
    gammaww00=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(-w;w,0,0)' in elem:
                xxxx=list[i+1]
                yyxx=list[i+2]
                zzxx=list[i+3]
                xxyy=list[i+4]
                yyyy=list[i+5]
                zzyy=list[i+6]
                xxzz=list[i+7]
                yyzz=list[i+8]
                zzzz=list[i+9]
                tensors_c=[xxxx,yyyy,zzzz,xxyy,yyxx,xxzz,zzxx,yyzz,zzyy]
                #(xxxx,yyyy,zzzz,xxyy,yyxx,xxzz,zzxx,yyzz,zzyy)
                if convention=="T":
                    g=gammamathKerrt(xxxx[unit],yyyy[unit],zzzz[unit],xxyy[unit],yyxx[unit],xxzz[unit],zzxx[unit],yyzz[1],zzyy[1])
                elif convention=="B":
                    g=gammamathKerrb(xxxx[unit],yyyy[unit],zzzz[unit],xxyy[unit],yyxx[unit],xxzz[unit],zzxx[unit],yyzz[1],zzyy[1])
                lined = ["Tot(Gamma)({})({})".format(namingUnits(unit), convention), g, "", ""]
                gammaww00.append(list[i])
                gammaww00.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        gammaww00.append(lined_component)
    return gammaww00

def Gamma2www0(list,name,convention,unit,components=False):
    gamma2www0=[]
    for i, elem in enumerate(list):
        for j, elem in enumerate(elem):
            if 'Gamma(-2w;w,w,0)' in elem:
                xxxx=list[i+1]
                yyxx=list[i+2]
                xyyx=list[i+3]
                zzxx=list[i+4]
                xzzx=list[i+5]
                yxxy=list[i+6]
                xyxy=list[i+7]
                yyyy=list[i+8]
                zzyy=list[i+9]
                yzzy=list[i+10]
                zxxz=list[i+11]
                zyyz=list[i+12]
                xzxz=list[i+13]
                yzyz=list[i+14]
                zzzz=list[i+15]
                #result=(3*((float(xxxx))/6)+((float(yyyy))/6)+((float(zzzz))/6))+(2*(((float(xyxy))/6)+((float(xzxz))/6)+((float(yzyz))/6)+((float(yxyx))/6)+((float(zxzx))/6)+((float(zyzy))/6)))+(((float(xyyx))/6)+((float(xzzx))/6)+((float(yxxy))/6)+((float(yzzy))/6)+((float(zxxz))/6)+((float(zyyz))/6))
                #xxxx,yyyy,zzzz,xyxy,xzxz,yzyz,yyxx,zzxx,zzyy,xyyx,xzzx,yxxy,yzzy,zxxz,zyyz):
                tensors_c=[xxxx,yyyy,zzzz,xyxy,xzxz,yzyz,yyxx,zzxx,zzyy,xyyx,xzzx,yxxy,yzzy,zxxz,zyyz]
                #ijkl = ikjl
                # Thus, xxzz=xzxz, yyzz=yzyz and xxyy=xyxy                
                if convention=="T":
                    g=gammamathEFISHt(xxxx[unit],yyyy[unit],zzzz[unit],xyxy[unit],xzxz[unit],yzyz[unit],yyxx[unit],zzxx[unit],zzyy[unit],xyyx[unit],xzzx[unit],yxxy[unit],yzzy[unit],zxxz[unit],zyyz[unit])
                elif convention=="B":
                    g=gammamathEFISHb(xxxx[unit],yyyy[unit],zzzz[unit],xyxy[unit],xzxz[unit],yzyz[unit],yyxx[unit],zzxx[unit],zzyy[unit],xyyx[unit],xzzx[unit],yxxy[unit],yzzy[unit],zxxz[unit],zyyz[unit])
                lined = ["Tot(Gamma)({})({})".format(namingUnits(unit), convention), g, "", ""]
                gamma2www0.append(list[i])
                gamma2www0.append(lined)
                if components == True:
                    for component in tensors_c:
                        lined_component= ["{} ({})".format(component[0],namingUnits(unit)),component[unit],"",""]
                        gamma2www0.append(lined_component)
    return gamma2www0

