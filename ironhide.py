# Ironhide - Extract key files from Illumina DRAGEN Server SOS reports
# Creator - L.Kraesing

## Importing Libraries ##
import warnings
warnings.filterwarnings('ignore')
import os
import tarfile as tf
import glob
import argparse

#### Helper Functions For Running ####
def change_dir():
    os.chdir(os.getcwd())
    print("Current working directory: {}".format(os.getcwd()))

def select_report():
    file_= glob.glob("*tar.xz")[0]
    return file_

def import_sos_report():
    file = select_report()
    sos_report = tf.open(r"{0}\{1}".format(os.getcwd(),file))
    return sos_report

## Run DEFAULT
def default_paths():
    paths_for_default_files = [
        "sos_commands/logs/",
        "sos_commands/hardware/dmidecode",
        "sos_commands/dragen/"]
    return paths_for_default_files

def create_initial_path_for_files():
    list_of_paths = []
    report = select_report()[:-7] + "/"
    for p_default in default_paths():
        list_of_paths.append(report + p_default)
    return list_of_paths

def fetch_file_paths():
    sos_report = import_sos_report()
    list_of_paths = create_initial_path_for_files()
    file_paths = []
    for f in list_of_paths:
        file = [f_name for f_name in sos_report.getnames() if f_name.startswith(f)]
        file_paths.append(file)
    return file_paths

## Run USER DEFINED
def user_def_list_of_paths():
    paths_and_files = "paths_and_files.txt"
    if os.path.exists(r"{0}\{1}".format(os.getcwd(),paths_and_files)):
        with open(paths_and_files, "r") as f:
            user_list = f.readlines()
            paths_for_user_def_files = []
            for line in user_list:
                line = line.split("\n")[0]
                paths_for_user_def_files.append(line)
    return paths_for_user_def_files

def create_initial_path_for_user_def_files():
    list_of_paths_user_def = []
    report = select_report()[:-7] + "/"
    paths_for_user_def_files = user_def_list_of_paths()
    for p_user in paths_for_user_def_files:
        list_of_paths_user_def.append(report + p_user)
    return list_of_paths_user_def

def fetch_file_paths_user_defined():
    sos_report = import_sos_report()
    list_of_paths = create_initial_path_for_user_def_files()
    file_paths = []
    for f in list_of_paths:
        file = [f_name for f_name in sos_report.getnames() if f_name.startswith(f)]
        file_paths.append(file)
    return file_paths

def extract_needed_files(file_paths):
    output_from_fetch_file_path = sum(file_paths, [])
    for file_ in output_from_fetch_file_path:
        print("Extracting file: {}".format(file_))
        with tf.open(r"{0}\{1}".format(os.getcwd(), select_report()), "r:xz") as _xz_file:
            _xz_file.extract(file_, path=os.getcwd())

def running_sos():
    change_dir()
    extract_needed_files(file_paths=fetch_file_paths())

def running_sos_user_defined():
    change_dir()
    extract_needed_files(file_paths=fetch_file_paths_user_defined())

def files_within_sosreport():
    change_dir()
    sos_report = import_sos_report()
    for i in sos_report.getnames():
        print(i)
        with open("files_within_sosreport.txt", mode="a") as files_within:
            files_within.write(str(f'{i}\n'))

#### ROLLING! ####
def main():
    parser = argparse.ArgumentParser(description="========== IRONHIDE ==========", epilog="Extract key files from Illumina DRAGEN Server SOS reports")
    parser.add_argument("-r", "--run", help="Extracting a default set of files", action="store_true")
    parser.add_argument("-u", "--user-defined", help="Extracting user-specified file(s) defined in paths_and_files.txt", action="store_true")
    parser.add_argument("-p", "--paths", help="Outputting all paths within the sos report into files_within_sosreport.txt", action="store_true")
    args = parser.parse_args()

    if args.run:
        running_sos()
    if args.user_defined:
        running_sos_user_defined()
    if args.paths:
        files_within_sosreport()

if __name__ == "__main__":
    main()