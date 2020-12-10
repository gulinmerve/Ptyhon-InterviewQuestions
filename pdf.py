import subprocess
import re
import glob, os
os.chdir(".") # In current directory
count = 1
for file in glob.glob('*.pdf'): # For all files with extension .pdf
    pdf_text = subprocess.getstatusoutput('pdf2txt.py ' + file)[1] # Get text content of the pdf file
    result = re.search('(\d{3} \d{3} \d{2} \d{2})\n(\d{2}).(\d{2}).(\d{4})', pdf_text) 
    # Search using a regex specific to your problem and find the date
    if result: # If date has been found
        new_name = result.group(4) + '-' + result.group(3) + '-' +  result.group(2) + '_' + result.group(1)
        # reorder the regex groups as you wish
        new_file_name = new_name.replace(' ','') # More trimming
        cmd = 'mv ' + file + ' ' + new_file_name + f'_{count}' + '.pdf' # This command will run in the terminal
        subprocess.getstatusoutput(cmd) # Rename file to date.pdf
    count += 1   
    print(cmd + ' :: Command executed.') # Show what command has been executed