
import subprocess, os       #Library to execute terminal or commandline commands
import glob                 #Library to import multiple files, sorted on bases of size

pdf_files =glob.glob("<folder_path>/*.pdf")   #importing a list of file
for p in pdf_files:
    cmd= "pdftotext " + p 
    p=subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE)
    p.wait()
    print(p)
    

