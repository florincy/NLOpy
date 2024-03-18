def check_and_write(atoms, file,preview,basis):
    for element in atoms:
        filename = "Basis_" + element + ".txt"  # Assuming the file extension is .txt
        pwd=f"/home/florincy/NLO/Basis/{basis}/"
        print(pwd)
        try:
            with open(pwd+filename, 'r') as basis_file:
                file_content = basis_file.readlines()
                file.writelines(file_content)
                file_content='\n'.join(file_content) 
                preview.append(file_content)
        except FileNotFoundError:
            print(f"File '{filename}' not found for atom '{element}'.")
        
def generate_input_file(chk_file, mem_size, nproc_count, functional, solvent, charge, multiplicity, xyz,freq,property,basis,inputpath):
    inputpath= inputpath + "/NLO-input.com"
    preview=[]
    with open(inputpath, 'w') as file:
        file.writelines(f"%chk={chk_file}\n")
        preview.append(f"%chk={chk_file}")
        file.writelines(f"%mem={mem_size}\n")
        preview.append(f"%mem={mem_size}")
        file.writelines(f"%nproc={nproc_count}\n")
        preview.append(f"%nproc={nproc_count}")
        print(solvent)
        if solvent != "None":
            solventConf = f"scrf=(iefpcm,read,solvent={solvent})"
        else:
            solventConf = ""
        
        file.writelines(f"#p {functional}/gen gfinput scf=maxcycle=200 polar=({property}) CPHF=RdFreq {solventConf}\n\n")
        preview.append(f"#p {functional}/gen gfinput scf=maxcycle=200 polar=({property}) CPHF=RdFreq {solventConf}\n")
        file.writelines("Polar\n\n")
        preview.append("Polar")
        file.writelines(f"{multiplicity} {charge}\n")
        preview.append(f"{multiplicity} {charge}")
        xyz = [line.strip() for line in xyz if line.strip()]
        content = '\n'.join(xyz) 
        print(content)
        file.writelines(content)
        preview.append(content)
        file.writelines('\n')

        file.writelines(f"\n{freq}nm\n\n")
        preview.append(f"\n{freq}nm\n\n")
        atoms=[]
        for line in xyz:
            # Split the line by spaces and strip each element to remove trailing spaces
            if line == "":
                pass
            else:
                formatted_line = [element.strip() for element in line.split()]
                # Append the formatted line to the list
                #print(formatted_line)
                atoms.append(formatted_line[0])
                atoms=list(set(atoms))
        #print(atoms)
        
        check_and_write(atoms,file ,preview,basis)
        preview = '\n'.join(preview) 
        with open("testin.com", 'w') as testin:
            testin.writelines(preview)
    return preview