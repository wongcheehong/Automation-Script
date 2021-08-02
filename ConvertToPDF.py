# Convert the PowerPoint PPTs to PDFs in the Working Folder

# Purpose: Converts the PowerPoint/Word to Adobe PDF in the working folder 

# Usage: python.exe ConvertHere.py

# Note: Uses the working folder (i.e. the folder containing the running script)
# Note: Also works with PPTX file format

import sys
import os
import comtypes.client

# Get path of running script
script_path = sys.argv[0]

# Get real path
real_path = os.path.realpath(script_path)

# Get directory path
folder_path = os.path.dirname(real_path)

# Add final slash at end
folder_path += "\\"

# Get files in input folder
input_file_paths = os.listdir(folder_path)

PDF_folder_path = folder_path + "PDF\\"
if not os.path.isdir(PDF_folder_path):
    os.mkdir(PDF_folder_path)

# Convert each file
for input_file_name in input_file_paths:

    # Skip if file does not contain a power point extension
    if input_file_name.lower().endswith((".ppt", ".pptx")):
        # Create input file path
        input_file_path = os.path.join(folder_path, input_file_name)
            
        # Create powerpoint application object
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        
        # Open the powerpoint slides
        slides = powerpoint.Presentations.Open(input_file_path)
        
        # Get base file name
        file_name = os.path.splitext(input_file_name)[0]
        
        # Create output file path
        output_file_path = os.path.join(PDF_folder_path, file_name + ".pdf")
        
        # Save as PDF (formatType = 32)
        slides.SaveAs(output_file_path, 32)
        
        # Close the slide deck
        slides.Close()
    elif input_file_name.lower().endswith((".doc", ".docx")):
        # Create input file path
        input_file_path = os.path.join(folder_path, input_file_name)

        # Create word application object
        word = comtypes.client.CreateObject("Word.Application")
        
        # Set visibility to False (Run in background)
        word.Visible = False

        # Open the word file
        doc = word.Documents.Open(input_file_path)

        # Get base file name
        file_name = os.path.splitext(input_file_name)[0]

        # Create output file path
        output_file_path = os.path.join(PDF_folder_path, file_name + ".pdf")
        
        # Save as PDF (formatType = 32)
        doc.SaveAs(output_file_path, FileFormat=17)
        
        # Close the slide deck
        doc.Close()
        word.Quit()
    else:
        continue

    print(f"Converted \"{file_name}\" to PDF")

try:
    powerpoint.Quit()
except NameError:
    pass
print("All conversion is completed")