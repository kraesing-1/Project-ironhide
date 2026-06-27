# Project Ironhide 
Creator - L. Kraesing
___________________________________________________
## A Tool designed to extract a set of specific files from Illumina DRAGEN SOS reports. 

Purpose: Access and extract only the files you need from a .tar.xz archive, avoiding a full unpack.
___________________________________________________
### Usage: 
Download the SOS report and keep it in its original .tar.xz format — no unpacking required.
From a command prompt or terminal, run the ironhide.py file with one of the three operational modes described below.
___________________________________________________
```bash
python /path/to/ironhide.py -r
```

Extracts a default set of files, including:
sos_commands/logs/
sos_commands/hardware/dmidecode
sos_commands/dragen/
___________________________________________________
```bash
python /path/to/ironhide.py -u
```
Extracts user-specified file(s) defined in 'paths_and_files.txt'
Looks for a paths_and_files.txt file in the same directory as the SOS report. If the file exists, it uses the paths listed within to extract specific files or directories.
e.g. 
version.txt
sos_commands/logs/journalctl_--no-pager_--boot
___________________________________________________
```bash
python /path/to/ironhide.py -p
```

Outputs all paths within the SOS report and saves them to 'files_within_sosreport.txt'
This lists all paths within the SOS report - useful when unsure of the exact location of a file 
___________________________________________________
```bash
python /path/to/ironhide.py -h
```

Shows the different option available.
___________________________________________________
### Process for converting the ironhide.py into an executable file with pyinstaller
The ironhide.py script can also be converted into an executable and run within the directory containing the SOS report as follows:

Pyinstaller packages the Python scripts into a standalone executable.
Run the following - if PyInstaller is not installed on the system for the convertion.
```bash
pip install pyinstaller
```
In the command prombt or terminal, run the following when PyInstaller is installed: 
```bash
pyinstaller --onefile ironhide.py
```

At first, several log messages will appear. The final one will indicate “completed successfully,” meaning the executable has been created successfully.

