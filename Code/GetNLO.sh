#!/bin/bash

Methods=('B3LYP' 'CAM-B3LYP')
#echo "."

# Prompt the user to select a directory and store the path in a variable
directory=$(zenity --title="Select the directory" --file-selection --directory)

# Concatenate the selected directory path with the file name to create the results file path
ResultsPath="$directory/Results.txt"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "$ResultsPath"
# Loop through each method in the Methods array
for i in "${!Methods[@]}"; do
  directory2="$directory/${Methods[i]}"
  cd "$directory2"
  
  # Find the input file with a .com extension in the directory and store the file name in a variable
  input=$(find "$directory2" -type f -name '*.com')
  
  # Get the base name of the input file and store it in a variable
  inputGAUSSIAN=$(basename -- "$input")
  
  # Create the output file name by replacing .com with .log and store it in a variable
  outputGAUSSIAN=$(basename -s .com "$input")".log"
  
  # Get the line number of the Energy and Dipole moment sections in the Gaussian output file
  NlinesEnergy="$(grep -n "Electric dipole moment (input orientation):" "$outputGAUSSIAN" | cut -d : -f 1)"
  NlinesDipoleMoment="$(grep -n "Electric dipole moment (dipole orientation):" "$outputGAUSSIAN" | cut -d : -f 1)"
  N=$(($NlinesDipoleMoment-$NlinesEnergy))
  
  # Extract the Energy and Dipole moment sections and write them to separate files
  grep "Electric dipole moment (input orientation):" "$outputGAUSSIAN" -B1 -A$N > EnergyReference.txt
  grep "Electric dipole moment (dipole orientation):" "$outputGAUSSIAN" -B1 -A$N > DipoleMomentReference.txt
  
  # Write the method name to the results file
  echo "METODO ${Methods[$i]}:" >> "$ResultsPath"
  
  # Check if the Beta(-w,w,0) field was requested in the input and write the results to the results file
  if grep -q "Beta(-w;w,0)" EnergyReference.txt; then
    echo "Beta(-w,w,0):" >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "x " EnergyReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "y " EnergyReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "z " EnergyReference.txt | head -n 1 >> "$ResultsPath"
  else
    #echo "Error: Field not requested in the input"
    :
  fi
    # Check if the Beta(-2w,w,w) field was requested in the input and write the results to the results file
  grep -q "Beta(-2w;w,w)" EnergyReference.txt
  if [ $? -eq 0 ]; then
    echo "Beta(-2w,w,w):" >> $directory/Results.txt
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "x " EnergyReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "y " EnergyReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "z " EnergyReference.txt | head -n 1 >> "$ResultsPath"
  else
    #echo "Erro: Campo não requisitado no input"
    :
  fi
  if grep -q "Beta(-w;w,0)" DipoleMomentReference.txt; then
    echo "Beta(-w,w,0):" >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "x " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "y " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-w;w,0)" -A7 * | xargs grep -w "z " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
  else
    #echo "Error: Field not requested in the input"
    :
  fi
    # Check if the Beta(-2w,w,w) field was requested in the input and write the results to the results file
  grep -q "Beta(-2w;w,w)" EnergyReference.txt
  if [ $? -eq 0 ]; then
    echo "Beta(-2w,w,w):" >> $directory/Results.txt
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "x " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "y " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
    grep -l "Beta(-2w;w,w)" -A7 * | xargs grep -w "z " DipoleMomentReference.txt | head -n 1 >> "$ResultsPath"
  else
    #echo "Erro: Campo não requisitado no input"
    :
  fi
done 
cd "$SCRIPT_DIR"
# Run the Python script with the results file path as an argument
python3 MakeATableForNLO.py "$ResultsPath"